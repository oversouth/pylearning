import pygame
import json
import math
import os
import time

# --- CONFIGURATION ---
WIDTH, HEIGHT = 1000, 700
FPS = 60
SAVE_FILE = "cookie_save.json"

# Colors
BG_COLOR = (25, 20, 20)
SIDEBAR_COLOR = (40, 35, 35)
PANEL_COLOR = (60, 55, 55)
ACCENT_COLOR = (255, 200, 50)
TEXT_WHITE = (255, 255, 255)
TEXT_GRAY = (180, 180, 180)
COOKIE_BROWN = (190, 130, 50)
CHIP_BROWN = (80, 40, 20)

# --- CLASSES ---

class Particle:
    """Rising +1 text effects."""
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.alpha = 255
        self.vel_y = -2
        self.life = 60 # frames

    def update(self):
        self.y += self.vel_y
        self.alpha -= 4
        self.life -= 1

    def draw(self, screen, font):
        if self.alpha > 0:
            surf = font.render(self.text, True, TEXT_WHITE)
            surf.set_alpha(self.alpha)
            screen.blit(surf, (self.x - surf.get_width()//2, self.y))

class Building:
    def __init__(self, name, icon, base_cost, base_cps):
        self.name = name
        self.icon = icon
        self.base_cost = base_cost
        self.base_cps = base_cps
        self.count = 0
        self.multiplier = 1.0

    @property
    def current_cost(self):
        return int(self.base_cost * (1.15 ** self.count))

    @property
    def cps_contribution(self):
        return self.count * self.base_cps * self.multiplier

class Upgrade:
    def __init__(self, uid, name, desc, cost, req_type, req_val, target, mult):
        self.uid = uid
        self.name = name
        self.desc = desc
        self.cost = cost
        self.req_type = req_type   # 'cookies' or 'building'
        self.req_val = req_val     # threshold to unlock
        self.target = target       # 'click' or building name
        self.mult = mult           # multiplier (usually 2.0)
        self.unlocked = False      # visible in shop
        self.purchased = False

class Cookie:
    def __init__(self):
        self.x, self.y = 325, 350
        self.base_radius = 120
        self.current_scale = 1.0
        self.angle = 0
        self.glow_angle = 0

    def update(self):
        # Idle rotation
        self.angle += 0.5
        self.glow_angle += 1
        # Smoothly return to scale 1.0
        if self.current_scale > 1.0:
            self.current_scale -= 0.02

    def draw(self, screen, total_cps):
        # 1. Golden Glow
        glow_pulse = math.sin(time.time() * 2) * 10
        glow_size = int(self.base_radius * 1.3 + min(total_cps * 0.1, 50) + glow_pulse)
        glow_surf = pygame.Surface((glow_size*2, glow_size*2), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (255, 215, 0, 80), (glow_size, glow_size), glow_size)
        screen.blit(glow_surf, (self.x - glow_size, self.y - glow_size), special_flags=pygame.BLEND_ADD)

        # 2. Main Cookie Body
        radius = int(self.base_radius * self.current_scale)
        pygame.draw.circle(screen, COOKIE_BROWN, (self.x, self.y), radius)
        pygame.draw.circle(screen, (210, 150, 70), (self.x, self.y), radius, 5) # Highlight edge

        # 3. Chocolate Chips (Rotating)
        for i in range(6):
            chip_angle = math.radians(self.angle + (i * 60))
            cx = self.x + math.cos(chip_angle) * (radius * 0.6)
            cy = self.y + math.sin(chip_angle) * (radius * 0.6)
            pygame.draw.circle(screen, CHIP_BROWN, (int(cx), int(cy)), radius // 8)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ultimate Cookie Clicker")
        self.clock = pygame.time.Clock()
        self.running = True

        # Fonts
        self.font_large = pygame.font.SysFont("Verdana", 42, bold=True)
        self.font_med = pygame.font.SysFont("Verdana", 24, bold=True)
        self.font_small = pygame.font.SysFont("Verdana", 16)
        self.font_tiny = pygame.font.SysFont("Verdana", 12)

        # Game Logic
        self.cookies = 0.0
        self.total_earned = 0.0
        self.cpc_multiplier = 1.0
        
        self.cookie_obj = Cookie()
        self.particles = []
        
        # Define Buildings
        self.buildings = [
            Building("Cursor", "🖱️", 15, 0.1),
            Building("Grandma", "👵", 100, 1),
            Building("Farm", "🚜", 1100, 8),
            Building("Factory", "🏭", 12000, 47),
            Building("Bank", "🏦", 130000, 260),
            Building("Temple", "🏛️", 1400000, 1400)
        ]

        # Define Upgrades
        self.upgrades = [
            Upgrade("up1", "Plastic Mouse", "Clicks x2", 100, "cookies", 50, "click", 2.0),
            Upgrade("up2", "Iron Mouse", "Clicks x2", 500, "cookies", 250, "click", 2.0),
            Upgrade("up3", "Forwards", "Grandmas x2", 1000, "building", 1, "Grandma", 2.0),
            Upgrade("up4", "Fertilizer", "Farms x2", 5000, "building", 5, "Farm", 2.0),
            Upgrade("up5", "Titanium Mouse", "Clicks x2", 10000, "cookies", 5000, "click", 2.0),
            Upgrade("up6", "Sweatshops", "Factories x2", 25000, "building", 10, "Factory", 2.0),
            Upgrade("up7", "Global Markets", "Banks x2", 250000, "building", 10, "Bank", 2.0),
            Upgrade("up8", "Deity Rituals", "Temples x2", 2000000, "building", 10, "Temple", 2.0),
        ]

        # UI State
        self.shop_scroll = 0
        self.notif_text = ""
        self.notif_timer = 0
        self.last_save = time.time()
        
        self.load_game()

    def get_total_cps(self):
        return sum(b.cps_contribution for b in self.buildings)

    def get_cpc(self):
        return 1.0 * self.cpc_multiplier

    def notify(self, text):
        self.notif_text = text
        self.notif_timer = 120 # 2 seconds

    def save_game(self):
        data = {
            "cookies": self.cookies,
            "total_earned": self.total_earned,
            "cpc_mult": self.cpc_multiplier,
            "counts": [b.count for b in self.buildings],
            "upgrades": [u.purchased for u in self.upgrades]
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)
        self.notify("Game Auto-saved!")

    def load_game(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    data = json.load(f)
                    self.cookies = data.get("cookies", 0)
                    self.total_earned = data.get("total_earned", 0)
                    self.cpc_multiplier = data.get("cpc_mult", 1.0)
                    counts = data.get("counts", [])
                    for i, count in enumerate(counts):
                        if i < len(self.buildings): self.buildings[i].count = count
                    
                    up_states = data.get("upgrades", [])
                    for i, bought in enumerate(up_states):
                        if i < len(self.upgrades) and bought:
                            u = self.upgrades[i]
                            u.purchased = True
                            u.unlocked = True
                            if u.target == "click": self.cpc_multiplier *= u.mult
                            else:
                                for b in self.buildings:
                                    if b.name == u.target: b.multiplier *= u.mult
            except: pass

    def handle_click(self, pos):
        # 1. Main Cookie Click
        dist = math.hypot(pos[0] - self.cookie_obj.x, pos[1] - self.cookie_obj.y)
        if dist <= self.cookie_obj.base_radius:
            val = self.get_cpc()
            self.cookies += val
            self.total_earned += val
            self.cookie_obj.current_scale = 1.1
            self.particles.append(Particle(pos[0], pos[1], f"+{val:g}"))
            return

        # 2. Upgrade Shop Clicks (Icons)
        # Rects match drawing logic: 660 + offset, 110, 45x45
        u_x = 660
        for u in self.upgrades:
            if u.unlocked and not u.purchased:
                u_rect = pygame.Rect(u_x, 110, 45, 45)
                if u_rect.collidepoint(pos):
                    if self.cookies >= u.cost:
                        self.cookies -= u.cost
                        u.purchased = True
                        if u.target == "click": self.cpc_multiplier *= u.mult
                        else:
                            for b in self.buildings:
                                if b.name == u.target: b.multiplier *= u.mult
                        self.notify(f"Unlocked: {u.name}!")
                    return
                u_x += 50

        # 3. Building Shop Clicks
        # Check if click is inside the sidebar area
        if pos[0] > 650 and pos[1] > 170:
            # Important: Adjust click for scroll offset
            relative_y = pos[1] - 170 - self.shop_scroll
            item_index = relative_y // 80
            if 0 <= item_index < len(self.buildings):
                b = self.buildings[int(item_index)]
                if self.cookies >= b.current_cost:
                    self.cookies -= b.current_cost
                    b.count += 1
                    self.notify(f"Bought {b.name}!")
                else:
                    self.notify("Not enough cookies!")

    def update(self):
        dt = 1/FPS
        self.cookie_obj.update()
        
        # Passive Income
        cps = self.get_total_cps()
        self.cookies += cps * dt
        self.total_earned += cps * dt

        # Update Particles
        for p in self.particles[:]:
            p.update()
            if p.life <= 0: self.particles.remove(p)

        # Check Upgrade Unlocks
        for u in self.upgrades:
            if not u.unlocked:
                if u.req_type == "cookies" and self.total_earned >= u.req_val:
                    u.unlocked = True
                elif u.req_type == "building":
                    for b in self.buildings:
                        if b.name == u.target and b.count >= u.req_val:
                            u.unlocked = True

        # Timers
        if self.notif_timer > 0: self.notif_timer -= 1
        if time.time() - self.last_save > 30:
            self.save_game()
            self.last_save = time.time()

    def draw(self):
        self.screen.fill(BG_COLOR)
        
        # --- LEFT AREA ---
        # Stats
        cookie_count_surf = self.font_large.render(f"{int(self.cookies):,} Cookies", True, ACCENT_COLOR)
        cps_surf = self.font_med.render(f"CPS: {self.get_total_cps():.1f}", True, TEXT_WHITE)
        self.screen.blit(cookie_count_surf, (325 - cookie_count_surf.get_width()//2, 50))
        self.screen.blit(cps_surf, (325 - cps_surf.get_width()//2, 105))
        
        self.cookie_obj.draw(self.screen, self.get_total_cps())
        for p in self.particles: p.draw(self.screen, self.font_med)

        # --- RIGHT SIDEBAR ---
        pygame.draw.rect(self.screen, SIDEBAR_COLOR, (650, 0, 350, HEIGHT))
        pygame.draw.line(self.screen, PANEL_COLOR, (650, 0), (650, HEIGHT), 3)

        # Upgrade Section
        shop_label = self.font_med.render("Store", True, TEXT_WHITE)
        self.screen.blit(shop_label, (660, 20))
        
        u_x = 660
        for u in self.upgrades:
            if u.unlocked and not u.purchased:
                color = ACCENT_COLOR if self.cookies >= u.cost else (100, 80, 20)
                u_rect = pygame.Rect(u_x, 110, 45, 45)
                pygame.draw.rect(self.screen, color, u_rect, border_radius=5)
                # Tooltip icon logic
                if u_rect.collidepoint(pygame.mouse.get_pos()):
                    # Simple tooltip
                    pygame.draw.rect(self.screen, (0,0,0), (660, 60, 330, 45))
                    t1 = self.font_tiny.render(f"{u.name}: {u.desc}", True, TEXT_WHITE)
                    t2 = self.font_tiny.render(f"Cost: {u.cost:,} cookies", True, ACCENT_COLOR)
                    self.screen.blit(t1, (665, 62))
                    self.screen.blit(t2, (665, 82))
                u_x += 50

        # Buildings List (Clipping Area)
        build_surface = pygame.Surface((340, 520))
        build_surface.fill(SIDEBAR_COLOR)
        
        for i, b in enumerate(self.buildings):
            by = i * 80 + self.shop_scroll
            b_rect = pygame.Rect(5, by, 320, 75)
            
            # Draw Item Card
            is_hover = b_rect.collidepoint((pygame.mouse.get_pos()[0]-650, pygame.mouse.get_pos()[1]-170))
            card_col = (80, 75, 75) if is_hover else (60, 55, 55)
            if self.cookies < b.current_cost: card_col = (45, 40, 40)
            
            pygame.draw.rect(build_surface, card_col, b_rect, border_radius=8)
            
            # Content
            name_txt = self.font_med.render(f"{b.icon} {b.name}", True, TEXT_WHITE)
            cost_col = ACCENT_COLOR if self.cookies >= b.current_cost else (200, 100, 100)
            cost_txt = self.font_small.render(f"Cost: {b.current_cost:,}", True, cost_col)
            count_txt = self.font_large.render(str(b.count), True, (255, 255, 255, 40))
            
            build_surface.blit(name_txt, (15, by + 10))
            build_surface.blit(cost_txt, (15, by + 40))
            build_surface.blit(count_txt, (260, by + 15))

        self.screen.blit(build_surface, (655, 170))

        # Milestone Notification Banner
        if self.notif_timer > 0:
            banner = pygame.Surface((WIDTH, 40))
            banner.set_alpha(min(255, self.notif_timer * 10))
            banner.fill((50, 150, 255))
            self.screen.blit(banner, (0, HEIGHT - 40))
            msg = self.font_small.render(self.notif_text, True, TEXT_WHITE)
            self.screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT - 30))

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_game()
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left Click
                        self.handle_click(event.pos)
                    if event.button == 4: # Scroll Up
                        self.shop_scroll = min(0, self.shop_scroll + 30)
                    if event.button == 5: # Scroll Down
                        self.shop_scroll = max(-300, self.shop_scroll - 30)

            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
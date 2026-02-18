import pyotp
import requests
import time
SECRET_KEY = "WT6UJNND3TLZGBCT"
BOT_TOKEN = "8504796102:AAHPgGgooVnu8oEN951wbebKt-4S59Q1JuE"
CHAT_ID = "5762415873"
totp = pyotp.TOTP(SECRET_KEY)
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
last_code = ""
while True:
    current_code = totp.now()
    remaining_time = totp.interval - int(time.time()) % totp.interval
    if current_code != last_code:
        message = f"github 2fa code: {current_code}\n{remaining_time}s left"
        try:
            requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        except Exception as e:
            print("failed to send:", e)
        last_code = current_code
    time.sleep(1)

player = {
    "username":"oversouth",
    "age":11,
    "gamerscore":8305
}

print(player.get('username'))
print(player["age"])
print(player["gamerscore"])

player["country"] = "Georgia"
print(player["country"])

print(player.keys())
print(player.values())
print(player.items())

player.pop('username')
player.popitem()
print(player.items())

for key in player.keys():
    print(key)

for value in player.values():
    print(value)

for item in player.items():
    print(item)
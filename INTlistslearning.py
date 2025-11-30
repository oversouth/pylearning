numbers = [10, 20, 30, 40, 50]
for number in numbers:
    if number > 25:
        print(number)

names = ["Max", "Pavel(Durov)","DOOM GUY", "sigma"]

for namedata in names:
    if namedata.startswith('M'):
        print(namedata)

Hvar = 0

for NBdata in numbers:
  Hvar += NBdata

print(Hvar)

gamers = [
    {'name': 'oversouth','gamerscore': 8350},
    {'name': 'doomguy', 'gamerscore': 4800},
    {'name': 'Scorpio', 'gamerscore': 2650},
    {'name': 'coolcoldy', 'gamerscore': 1800}
]

for gamer in gamers:
    gamer['gamerscore']
    if gamer['gamerscore'] > 2500:
       print(gamer['name'])

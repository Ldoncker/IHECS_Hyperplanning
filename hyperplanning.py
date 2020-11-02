import requests
import urllib.request
from datetime import date

group = 'A'

url = "http://horaires.ihecs.be/_ressource.js"
js = requests.get(url)

f = open("ressource.txt", "w")
f.write(js.text)
f.close()

f = open("ressource.txt", "r")
bloc1 = ""

for i, line in enumerate(f):
	if i >= 199 and i <= 215:
		cpt = 0
		while cpt < len(line):
			if cpt > 78 and cpt < 96:
				bloc1 += line[cpt]
			cpt += 1
f.close()

allgroups = bloc1.split('"')
cpt = 0
for i in allgroups:
	if len(i) > 1 and i[1] == group:
		p1 = allgroups[allgroups.index(i) + 2]

p2 = "S000000000"

x = date.today()
day = int(x.strftime("%d"))
month = int(x.strftime("%m"))

if month == 10:
	p2 += "0040"
elif month == 11:
	if day == 1:
		p2 += "0040"
	elif day < 9:
		p2 += "0080"
	elif day < 16:
		p2 += "0100"
	elif day < 23:
		p2 += "0200"
	elif day < 30:
		p2 += "0400"
	else:
		p2 += "0800"
elif month == 12:
	if day < 7:
		p2 += "0800"
	elif day < 14:
		p2 += "1000"
	else:
		p2 += "2000"

url = "http://horaires.ihecs.be/diplomes/" + p1 + p2 + ".png"

urllib.request.urlretrieve(url, p1 + p2 + ".png")

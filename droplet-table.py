
import sys
import json

data = json.load(sys.stdin)

print data

for index, droplet in enumerate(data["droplets"]):
    name = droplet["name"]
    id = droplet["id"]
    ipv4 = droplet["networks"]["v4"][0]["ip_address"]

    print "%s %s %s" % (name, id, ipv4)

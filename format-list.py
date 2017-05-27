
import sys
import json

data = json.load(sys.stdin)

for index, droplet in enumerate(data["droplets"]):
    no = index + 1

    id = droplet["id"]
    name = droplet["name"]
    ipv4 = droplet["networks"]["v4"][0]["ip_address"]
    os = "%s %s" % (droplet["image"]["distribution"], droplet["image"]["name"])

    region = droplet["region"]["slug"]
    size = droplet["size_slug"]
    image = droplet["image"]["slug"]

    print "%s. %s(%s) [%s] %s" % (no, name, id, ipv4, os)
    print "image: %s, size: %s, region: %s" % (image, size, region)

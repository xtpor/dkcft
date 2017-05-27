#!/bin/sh

# create the eula
echo "eula=true" > /minecraft/template/eula.txt

for file in /minecraft/template/*; do
    yes n | cp -i $file /minecraft/data/ 2> /dev/null
done

if ! grep -q enable-rcon /minecraft/data/server.properties; then
    echo enable rcon
    echo "enable-rcon=true" >> /minecraft/data/server.properties
fi

if ! grep -q rcon.password /minecraft/data/server.properties; then
    echo generate password
    echo "rcon.password=$( < /dev/urandom tr -dc 0-9a-f | head -c40  )" >> /minecraft/data/server.properties
fi

cd /minecraft/data

while true; do
    java -jar ../server.jar
    sleep 10
done


FROM openjdk:8-alpine

ARG VER

RUN mkdir /minecraft && mkdir /minecraft/data

COPY server.jar startup.sh minecraft/

COPY template minecraft/template/

CMD sh /minecraft/startup.sh

---
title: "Controling window blinds with esp32"
summary: ""
date: "May 16 2024"
draft: false
tags:
- esp32
- mqtt
repoUrl: "https://gitlab.etiam.si/grega.rotar/roleta"
authors:
- Grega Rotar
---
## PubSubClient installation
Install PubSubClient from:
```
https://github.com/knolleary/pubsubclient
```
- Ne pozabi dodat da se nastavijo vsi pin mode
- ne pozabi na subscrbe na vse topice
- const char *mqttBaseTopic = "/iot/roleta/babi";
- če je rcuid je za rolete
- če je lbuid je za žarnice
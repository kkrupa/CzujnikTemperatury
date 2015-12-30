# -*- coding: utf-8 -*-
import time
from czujnik import Czujnik
from api import Api

czujnik = Czujnik(4)
przesylacz = Api()

while True:
    temperature, humidity = czujnik.odczyt()
    przesylacz.sendData(temperature, humidity)
    time.sleep(60)

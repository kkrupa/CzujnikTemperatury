# -*- coding: utf-8 -*-
import Adafruit_DHT


class Czujnik:

    def __init__(self, sensorPin, sensorType=Adafruit_DHT.DHT11):
        self.sensorPin = sensorPin
        self.sensorType = sensorType

    def odczyt(self):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensorType, self.sensorPin)
            return temperature, humidity
        except IOError:
            print('Unable to read from the sensor. Try again!')
            return 0, 0

if __name__ == '__main__':
    czujnik = Czujnik(4)
    temperature, humidity = czujnik.odczyt()
    print('%s: %-.1f, %s: %-.0f' % ('Temperatura', temperature, 'Wilgotnosc', humidity))




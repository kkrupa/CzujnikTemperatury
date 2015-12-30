# -*- coding: utf-8 -*-
import httplib
import urllib


class Api:

    def __init__(self):
        self.headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        self.conn = httplib.HTTPConnection("api.thingspeak.com:80")

    def sendData(self, temperature, humidity):
        params = urllib.urlencode({'field1': temperature, 'field2': humidity, 'key': 'ECIONS53YTKYDB1X'})
        try:
            self.conn.request("POST", "/update", params, self.headers)
            response = self.conn.getresponse()
            print((temperature, humidity))
            print((response.status, response.reason))
            data = response.read()
            self.conn.close()
        except:
            print("Connection failed")

if __name__ == "__main__":
    przesylacz = Api()
    przesylacz.sendData(45, 25)
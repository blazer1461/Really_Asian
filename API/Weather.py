__author__ = 'blazer1461'
import urllib2
import json

def get_weather(city):
    url= "http://api.openweathermap.org/data/2.5/weather?q=" +city
    u= urllib2.urlopen(url)
    result= u.read();
    w= json.loads(result)
    t=w["main"]["temp"]
    f= 1.8 * (t-273)+32
    return f



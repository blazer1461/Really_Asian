__author__ = 'blazer1461'
import Weather
from flask import Flask, render_template

Asian_Weather= Flask(__name__)

@Asian_Weather.route('/<city>')
def city(city):
    temp= Weather.get_weather(city)
    return render_template("asian.html", temp_weather= temp)

if __name__ == "__main__":

    Asian_Weather.debug= True
    Asian_Weather.run(host= '0.0.0.0', port= 12345)


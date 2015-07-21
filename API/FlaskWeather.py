__author__ = 'blazer1461'
import Weather
from flask import Flask, render_template, request

Asian_Weather= Flask(__name__)

@Asian_Weather.route("/", methods=["POST", "GET"])
def main_page():
    if request.method == "GET":
        return render_template("base.html", city= "Main Page")
    elif request.method == "POST":
        city= request.form["location"]
        temp= Weather.get_weather(city)
        if temp > 80:
            location=  "kitchen"
        elif temp<80 and temp > 60:
            location= "dining room"
        else:
            location= "cellar"
        return render_template("weatherincity.html", temp_weather=temp, city=city +" weather", house= location , location=city)

if __name__ == "__main__":

    Asian_Weather.debug= True
    Asian_Weather.run(host= '0.0.0.0', port= 12345)


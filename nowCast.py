#!/usr/bin/env/ python

import requests, re
from bs4 import BeautifulSoup

response = requests.get('http://weather.uky.edu/ky/kyco_now_daily2.php')
soup = BeautifulSoup(response.content, "html.parser")

soupText = soup.get_text()

soupFix = soupText.replace("UKAWC Point Agricultural, Lawn & Garden Forecast/Outlook Kentucky Counties","").replace("*GDD-Growing Degree Days. Acc.GDD-Accumulated from Apr.1 to date.", ";").replace("\n","")

countyList = soupFix.split(";")

for x in countyList[14:15]:
    bullitt = x.split(",")

stats = bullitt[1].split("  ")

# Collects the current weather stats
nowRaw = stats[0]
nowFix = nowRaw.replace("KYNowcast","").replace("Dewpoint",",").replace("Windspeed",",").replace("Humidity",",").replace("Probabilty of Precip",",").replace("Spraying ConditionsDrying ConditionsLivestock StressDaily Forecast Summary DAY ","").replace("SAT","").replace("SUN","").replace("MON","").replace("TUE","").replace("WED","").replace("THU","").replace("FRI","")
nowList = nowFix.split(",")
currentTemp = nowList[0]
currentHum = nowList[3]
currentWind = nowList[2]
currentDewPoint = nowList[1]
currentRain = nowList[4]
print("Bullitt County Current Weather Conditions:")
print("Current Temp: " + currentTemp + "\n" + "Current Humidity: " + currentHum + "\n" + "Current Windspeed: " + currentWind + "\n" + "Current Dew Point: " + currentDewPoint + "\n" + "Current Chance of Precipitation: " + currentRain)

#Collects the temperature 7 day forecast
tempRaw = ''
tempRaw = stats[9]
tempSat = "SAT - HIGH: " + tempRaw[1:3] + "  LOW: " + tempRaw[6:8]
tempSun = "SUN - HIGH: " + tempRaw[8:10] + "  LOW: " + tempRaw[13:15]
tempMon = "MON - HIGH: " + tempRaw[15:17] + "  LOW: " + tempRaw[20:22]
tempTue = "TUE - HIGH: " + tempRaw[22:24] + "  LOW: " + tempRaw[27:29]
tempWed = "WED - HIGH: " + tempRaw[29:31] + "  LOW: " + tempRaw[34:36]
tempThu = "THU - HIGH: " + tempRaw[36:38] + "  LOW: " + tempRaw[41:43]
tempFri = "FRI - HIGH: " + tempRaw[43:45] + "  LOW: " + tempRaw[48:50]
#print("Bullitt County Temp Forecast:")
#print(tempSat + "\n" + tempSun + "\n" + tempMon + "\n" + tempTue + "\n" + tempWed + "\n" + tempThu + "\n" + tempFri + "\n") 

#Collects windspeed 7 day forecast
windSpeed = stats[24]
windFix = windSpeed.replace(" / ",",").replace(" ",",")
windList = windFix.split(",")
windHighSat = windList[0]
windLowSat = windList[1]
windHighSun = windList[2]
windLowSun = windList[3]
windHighMon = windList[4]
windLowMon = windList[5]
windHighTue = windList[6]
windLowTue = windList[7]
windHighWed = windList[8]
windLowWed = windList[9]
windHighThu = windList[10]
windLowThu = windList[11]
windHighFri = windList[12]
windLowFri = windList[13]
#print("Bullitt County Windspeed Forecast")
'''
print("Sat Windspeed High: "+windHighSat+" mph")
print("Sat Windspeed Low: "+windLowSat+" mph")
print("Sun Windspeed High: "+windHighSun+" mph")
print("Sun Windspeed Low: "+windLowSun+" mph")
print("Mon Windspeed High: "+windHighMon+" mph")
print("Mon Windspeed Low: "+windLowMon+" mph")
print("Tue Windspeed High: "+windHighTue+" mph")
print("Tue Windspeed Low: "+windLowTue+" mph")
print("Wed Windspeed High: "+windHighWed+" mph")
print("Wed Windspeed Low: "+windLowWed+" mph")
print("Thu Windspeed High: "+windHighThu+" mph")
print("Thu Windspeed Low: "+windLowThu+" mph")
print("Fri Windspeed High: "+windHighFri+" mph")
print("Fri Windspeed Low: "+windLowFri+" mph")
'''
#!/usr/bin/env/ python

import requests, re
from bs4 import BeautifulSoup

'''
webpage_response = requests.get('http://weather.uky.edu/ky/forecast.php#KY_County_Forecast')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
'''

response2 = requests.get('http://weather.uky.edu/ky/kyco_now_daily2.php')
soup2 = BeautifulSoup(response2.content, "html.parser")

#data2 = soup2.find_all("table", attrs={"class": "curr_condition"})
#data3 = soup2.find_all("table", attrs={"class": "Forecast"})

soupText = soup2.get_text()

soupFix = soupText.replace("UKAWC Point Agricultural, Lawn & Garden Forecast/Outlook Kentucky Counties","").replace("*GDD-Growing Degree Days. Acc.GDD-Accumulated from Apr.1 to date.", ";").replace("\n","")

countyList = soupFix.split(";")

tempFix = []
tempRaw = ''

for x in countyList[14:15]:
    bullitt = x.split(",")
    stats = bullitt[1].split("  ")
    tempRaw = stats[9]
    tempSat = "SAT - HIGH: " + tempRaw[1:3] + "  LOW: " + tempRaw[6:8]
    tempSun = "SUN - HIGH: " + tempRaw[8:10] + "  LOW: " + tempRaw[13:15]
    tempMon = "MON - HIGH: " + tempRaw[15:17] + "  LOW: " + tempRaw[20:22]
    tempTue = "TUE - HIGH: " + tempRaw[22:24] + "  LOW: " + tempRaw[27:29]
    tempWed = "WED - HIGH: " + tempRaw[29:31] + "  LOW: " + tempRaw[34:36]
    tempThu = "THU - HIGH: " + tempRaw[36:38] + "  LOW: " + tempRaw[41:43]
    tempFri = "FRI - HIGH: " + tempRaw[43:45] + "  LOW: " + tempRaw[48:50]
    humRaw = stats[16]
    humSat = "SAT - HIGH: " + humRaw[0:2] + "  LOW: " + humRaw[5:7]
    humSun = "SUN - HIGH: " + humRaw[8:10] + "  LOW: " + humRaw[13:15]
    humMon = "MON - HIGH: " + humRaw[16:18] + "  LOW: " + humRaw[21:23]
    humTue = "TUE - HIGH: " + humRaw[24:26] + "  LOW: " + humRaw[29:31]
    humWed = "WED - HIGH: " + humRaw[32:34] + "  LOW: " + humRaw[37:39]
    humThu = "THU - HIGH: " + humRaw[40:42] + "  LOW: " + humRaw[45:47]
    humFri = "FRI - HIGH: " + humRaw[48:50] + "  LOW: " + humRaw[53:55]
    print("Bullitt County Forecast:")
    print("Temperature (deg F):")
    print(tempSat + "\n" + tempSun + "\n" + tempMon + "\n" + tempTue + "\n" + tempWed + "\n" + tempThu + "\n" + tempFri) 
    print("Humidity (rH%):")
    print(humSat + "\n" + humSun + "\n" + humMon + "\n" + humTue + "\n" + humWed + "\n" + humThu + "\n" + humFri) 
    

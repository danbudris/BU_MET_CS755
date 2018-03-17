import math
import calendar
import datetime
from pyspark import SparkContext, SparkConf

## Initlize the spark context
sc = SparkContext()

## TASK 2
# calculate the cell ID
def getCellID(lat, lon):
    lat = float(lat)
    lon = float(lon)
    return (str(round(lat, 2)) + "-"+str(round(lon, 2)))

# calculate if the day is a sunday or not
def isWeekday(year, month, day):
    year    = int(year)
    month   = int(month)
    day     = int(day)
    dayCode = calendar.weekday(year, month, day)
    if dayCode == 6:
        return "Sunday"
    else:
        return "NotSunday"

# load the dataset
ride = sc.textFile("/Users/Dan/Desktop/taxi-data-sorted-small.csv.bz2")

# set up the function for returning the values
def getDropOffs(input, day):
    input\
    .filter(lambda x: ((x.split(",")[3].split(" ")[1] <= "11:00:00") & (x.split(",")[3].split(" ")[1] >= "08:00:00")))\
    .map(lambda x: (isWeekday((x.split(",")[3]).split(" ")[0].split("-")[0],(x.split(",")[3]).split(" ")[0].split("-")[1],(x.split(",")[3]).split(" ")[0].split("-")[2]), (x.split(",")[8], x.split(",")[9])))\
    .map(lambda x: (getCellID(x[1][1],x[1][0]), x[0]))\
    .filter(lambda x: x[1] == day)\
    .groupByKey()\
    .map(lambda x: (x[0], list(x[1]).count(day)))\
    .filter(lambda x: x[1] > 100)\
    .saveAsTextFile("/Users/Dan/Desktop/Task2Output-{}/".format(day))

getDropOffs(ride, "Sunday")
getDropOffs(ride, "NotSunday")
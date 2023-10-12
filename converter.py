import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

pressureData = pd.read_csv(r"C:\Users\tgalyon\Documents\python\data_directory\data.csv",index_col=False,skiprows=6)
time = []
pressure = []

time = pressureData.iloc[:,0]
pressure = pressureData.iloc[:,1]

def getDate(inputTime):
    global finalDateList
    global monthDay
    finalDateList = []
    monthDay = []
    for i in inputTime:
        dateFormat = "%m/%d/%Y %H:%M:%S %p"
        n = datetime.strptime(i,dateFormat).date()
        finalDateList.append(n)
    

def getUniqueDay(inputDate):
    global uniqueDay
    uniqueDay = []
    for i in inputDate:
        if i not in uniqueDay:
            uniqueDay.append(i)

def removeZeros(inputData,inputTime):
    global finalTime
    global finalPressure
    global finalDate
    finalTime = []
    finalPressure = []
    finalDate = []
    index = 0
    for item in inputData:
        if item > 10:
            finalPressure.append(item)
            finalTime.append((5 + (index * 5))/(24*60))
            finalDate.append(finalDateList[index])
            index += 1
    for i in finalDate:
        monthDay.append(str(i.month)+str(i.day))

def cleanData(inputData,inputTime,inputDate):
    for i in range(5):
        inputData.pop()    
        inputTime.pop()
        inputDate.pop()

def getDailyAverage(uniqueData, inputTime, finalPressure):
    tempSum = []
    global dailyAverage
    global dailyMax
    global dailyMin
    dailyAverage = []
    dailyMax = []
    dailyMin = []
    for i in uniqueData:
        for idn, n in enumerate(inputTime):
            if i == n:
                if idn == (len(inputTime) - 1):
                    tempSum.append(finalPressure[inputTime.index(n)])
                    dailyAverage.append(np.average(tempSum))
                    dailyMax.append(np.max(tempSum))
                    dailyMin.append(np.min(tempSum))
                    tempSum.clear()
                else:
                    tempSum.append(finalPressure[inputTime.index(n)])

def getAverage(input):
    global averageDailyMean
    averageDailyMean = np.average(input)

def getMax(input):
    global averageDailyMax
    averageDailyMax = np.average(input)

def getMin(input):
    global averageDailyMin
    averageDailyMin = np.average(input) 

getDate(time) 
removeZeros(pressure, time)
getUniqueDay(monthDay)
getDailyAverage(uniqueDay, monthDay, finalPressure)
getAverage(dailyAverage)
getMax(dailyMax)
getMin(dailyMin)

print(dailyAverage)
print(averageDailyMean)
print(averageDailyMax)
print(averageDailyMin)

#getAverage(dailyAverage)
#print("Min: " + str(min))
#print("Max: " + str(max))
#print("Average "  + str(dailyMean))
data = {"Date of Reading": finalDate, "Time (Days)": finalTime, "Pressure": finalPressure,}

df = pd.DataFrame(data)
df.to_csv(r"C:\Users\tgalyon\Documents\python\data_directory\out.csv")

plt.plot(finalTime,finalPressure)
plt.title("Pressure vs. Time")
plt.xlabel("Time (Days)")
plt.ylabel("Pressure (psi)")
plt.xticks(np.arange(np.min(finalTime), np.max(finalTime), 1))
plt.grid()
plt.show()
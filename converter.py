import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

pressureData = pd.read_csv(r"C:\Users\tgalyon\Desktop\data_directory\data.csv",index_col=False,skiprows=6)
time = []
pressure = []

time = pressureData.iloc[:,0]
pressure = pressureData.iloc[:,1]

def getDate(inputTime):
    global finalDateList
    finalDateList = []
    for i in inputTime:
        dateFormat = "%m/%d/%Y %H:%M:%S %p"
        n = datetime.strptime(i,dateFormat).date()
        finalDateList.append(n)
        

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

def cleanData(inputData,inputTime,inputDate):
    for i in range(5):
        inputData.pop()    
        inputTime.pop()
        inputDate.pop()

def getStats(finalPressure):
    global min
    global max
    global mean
    min = np.min(finalPressure)
    max = np.max(finalPressure)
    mean = np.round(np.mean(finalPressure))
    
getDate(time)  
removeZeros(pressure, time)
cleanData(finalPressure, finalTime, finalDate)
getStats(finalPressure)
print("Min: " + str(min))
print("Max: " + str(max))
print("Average "  + str(mean))
data = {"Date of Reading": finalDate, "Time (Days)": finalTime, "Pressure": finalPressure, "Min": min, "Max": max, "Average": mean}

df = pd.DataFrame(data)
df.to_csv(r"C:\Users\tgalyon\Desktop\data_directory\out.csv")

plt.plot(finalTime,finalPressure)
plt.title("Pressure vs. Time")
plt.xlabel("Time (Days)")
plt.ylabel("Pressure (psi)")
plt.xticks(np.arange(np.min(finalTime), np.max(finalTime), 1))
plt.grid()
plt.show()
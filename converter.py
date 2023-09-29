import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pressureData = pd.read_csv(r"C:\Users\tgalyon\Desktop\data_directory\data.csv",index_col=False,skiprows=6)
time = []
pressure = []

time = pressureData.iloc[:,0]
pressure = pressureData.iloc[:,1]

def removeZeros(inputData,inputTime):
    global finalTime
    global finalPressure
    finalTime = []
    finalPressure = []
    index = 0
    for item in inputData:
        if item > 10:
            finalPressure.append(item)
            finalTime.append(inputTime[index])
            index += 1

def cleanData(inputData,inputTime):
    for number in range(5):
        inputData.pop()    
        inputTime.pop()

def getStats(finalPressure):
    global min
    global max
    global mean
    min = np.min(finalPressure)
    max = np.max(finalPressure)
    mean = np.mean(finalPressure)
    
removeZeros(pressure, time)
cleanData(finalPressure, finalTime)
getStats(finalPressure)
print(min)
print(max)
print(mean)

data = {"Time": finalTime, "Pressure": finalPressure, "Min": min, "Max": max, "Average": mean}

df = pd.DataFrame(data)
df.to_csv(r"C:\Users\tgalyon\Desktop\data_directory\out.csv")

plt.plot(finalTime,finalPressure)
plt.title("Pressure vs. Time")
plt.xlabel("Time")
plt.ylabel("Pressure (psi)")
plt.show()
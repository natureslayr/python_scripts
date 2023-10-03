import pandas as pd
from datetime import datetime

billingData = pd.read_csv(r"C:\Users\tgalyon\Desktop\billing\billing.csv")
columns = list(billingData)

accountNumberIndex = 0
nameIndex = 0
addressIndex = 0
typeIndex = 0
readingDateIndex = 0
usageReadingIndex = 0
lowerCaseColumns = []

for i in columns:
    lowerCaseColumns.append(i.lower())

for i in lowerCaseColumns:
    if i == "account number full":
        accountNumberIndex = lowerCaseColumns.index(i)
    elif i == "name":
        nameIndex = lowerCaseColumns.index(i)
    elif i == "service address full":
        addressIndex = lowerCaseColumns.index(i)
    elif i == "address type":
        typeIndex = lowerCaseColumns.index(i)
    elif i == "reading date":
        readingDateIndex = lowerCaseColumns.index(i)
    elif i == "meter usage":
        usageReadingIndex = lowerCaseColumns.index(i)

accountNumber = billingData.iloc[:,accountNumberIndex]
name = billingData.iloc[:,nameIndex]
address = billingData.iloc[:,addressIndex]
accountType = billingData.iloc[:,typeIndex]
readingDate = billingData.iloc[:,readingDateIndex]
meterUsage = billingData.iloc[:,usageReadingIndex]
accountNumberList = []
meterUsageList = []
date = []
month = []
year = []
monthYear = []
uniqueMonthYear = []
uniqueAccountNumber = []
uniqueType = []
formatDate = '%m/%d/%Y'

for i in readingDate:
    date.append(datetime.strptime(i, formatDate).date())

for i in date:
    if i.month < 10:
        monthYear.append(str(i.month) + str(i.year))
    else:
        monthYear.append(str(i.month) + str(i.year))

for i in monthYear:
    if i not in uniqueMonthYear:
        uniqueMonthYear.append(i)

for i in accountNumber:
    accountNumberList.append(i)
    if i not in uniqueAccountNumber:
        uniqueAccountNumber.append(i)

for i in meterUsage:
    meterUsageList.append(i)

def getAverageList(uniqueList, nonUniqueList, usageData):
    tempSumList = []
    listLocation = 0
    global averageUsage 
    averageUsage = []
    for i in uniqueList:
        for n in nonUniqueList:
            if n == i:
                if listLocation == len(nonUniqueList) - 1:
                    if len(tempSumList) == 0:
                        averageUsage.append(0) 
                        tempAverage = 0
                        listLocation = 0
                        tempSumList.clear()
                    else:
                        tempAverage = (sum(tempSumList) / len(tempSumList))
                        averageUsage.append(tempAverage / (30.4*24*60)) 
                        tempAverage = 0
                        listLocation = 0
                        tempSumList.clear()
                else:
                    tempSumList.append(usageData[listLocation])
                    listLocation += 1
            else:
                if listLocation == len(nonUniqueList) - 1:
                    if len(tempSumList) == 0:
                        averageUsage.append(0) 
                        tempAverage = 0
                        listLocation = 0
                        tempSumList.clear()
                    else:
                        tempAverage = (sum(tempSumList) / len(tempSumList))
                        averageUsage.append(tempAverage / (30.4*24*60)) 
                        tempAverage = 0
                        listLocation = 0
                        tempSumList.clear()
                else:
                    listLocation += 1

def getPeakList(uniqueList, nonUniqueList, usageData):
    tempMaxList = []
    listLocation = 0
    global maxMonth
    global peakUsage
    global peakDict
    peakUsage = []
    peakDict = {}
    for i in uniqueList:
        for n in nonUniqueList:
            if n == i:
                if listLocation == len(nonUniqueList) - 1:
                    tempMaxList.append(usageData[listLocation])
                    peakUsage.append(max(tempMaxList)/(30.4*24*60))
                    listLocation = 0
                    tempMaxList.clear()
                else:
                    tempMaxList.append(usageData[listLocation])
                    listLocation += 1
            else:
                if listLocation == len(nonUniqueList) - 1:
                    peakUsage.append(max(tempMaxList)/(30.4*24*60))
                    listLocation = 0
                    tempMaxList.clear()
                else:
                    listLocation += 1
    for key in uniqueList:
        for value in peakUsage:
            peakDict[key] = value
            break
    maxMonth = (max(peakDict, key = peakDict.get))

def getPeakMonth(uniqueList, nonUniqueList, usageData, MonthYear):
    listLocation = 0
    global peakData
    peakData = []
    for i in uniqueList:
        for n in nonUniqueList:
            if n == i:
                if listLocation == len(nonUniqueList) - 1:
                    if MonthYear[listLocation] == maxMonth:
                        peakData.append(usageData[listLocation]/(30.4*24*60))
                        listLocation = 0
                    else:
                        listLocation = 0
                else:
                    if MonthYear[listLocation] == maxMonth:
                        peakData.append(usageData[listLocation]/(30.4*24*60))
                        listLocation += 1
                    else:
                        listLocation += 1
            else:
                peakData.append(0)

getAverageList(uniqueAccountNumber, accountNumberList, meterUsageList)
getPeakList(uniqueMonthYear, monthYear, meterUsageList)
getPeakMonth(uniqueAccountNumber, accountNumberList, meterUsageList, monthYear)
print(sum(peakData))
print(sum(averageUsage))

data = {
        "uniqueAccountNumber": pd.Series(uniqueAccountNumber),
        "averageDemand": pd.Series(averageUsage),
        "peakDemand": pd.Series(peakData)
        }

df = pd.DataFrame(data)

for i in uniqueMonthYear:
    df[i] = ""

df.to_csv(r"C:\Users\tgalyon\Desktop\billing\out.csv")
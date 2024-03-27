import pandas as pd

inputData = pd.read_csv(r"/home/tyler/Documents/SCADA/input/input.csv",index_col=False, skiprows=1)

date = []
time = []
description = []
value = []

date = inputData.iloc[:,0]
time = inputData.iloc[:,1]
description = inputData.iloc[:,3]
value = inputData.iloc[:,4]

def findUniqueDescription(inputScript):
  global uniqueDescription
  uniqueDescription = []
  for i in inputScript:
    if i not in uniqueDescription:
      uniqueDescription.append(i)

def getValues(inputUniqueValues,inputScript,inputValues):
  global d
  d = dict()
  p = 0
  for i in inputUniqueValues:
    d.update({i:[]})
  for n in inputScript:
    if n in inputUniqueValues:
      d[n].append(inputValues[p])
      p+=1

def getUniqueDates(date):
  global uniqueDate
  uniqueDate = []
  for i in date:
    if i not in uniqueDate:
      uniqueDate.append(i)

def getUniqueTime(time):
  global uniqueTime
  uniqueTime = []
  for i in time:
    if i not in uniqueTime:
      uniqueTime.append(i)

findUniqueDescription(description)
getValues(uniqueDescription,description,value)
getUniqueDates(date)
getUniqueTime(time)

keys = d.keys()
values = d.values()

data = {
    "Keys":pd.Series(keys),
    "Values": pd.Series(values)    
    }

df = pd.DataFrame(data)
df.to_csv(r"/home/tyler/Documents/SCADA/input/midway.csv")

midwayData = pd.read_csv(r"/home/tyler/Documents/SCADA/input/midway.csv",index_col=False, skiprows=1)


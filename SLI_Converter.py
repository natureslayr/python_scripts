import pandas as pd

inputData = pd.read_csv(r"Z:\01305-0008\02-Engineering\03-Utilities\01_Service_Line_Inventory\Service_Line_Converter\input.csv", \
                        low_memory=False, index_col=False, skiprows=2)

Account_ID = inputData.iloc[:,1]
Address = inputData.iloc[:,2]

Utility_Material = inputData.iloc[:,7]
Utility_Install_Date = inputData.iloc[:,10]
Utility_Source = inputData.iloc[:,11]
Utility_Verification_Method = inputData.iloc[:,13]
Utility_Status = inputData.iloc[:,15]

Customer_Material = inputData.iloc[:,18]
Customer_Install_Date = inputData.iloc[:,20]
Customer_Source = inputData.iloc[:,21]
Customer_Verification_Method = inputData.iloc[:,23]
Customer_Status = inputData.iloc[:,25]

Comments = inputData.iloc[:,61]
Occupancy_Type = inputData.iloc[:,31]

Material = []
Utility_Material_Detail = []
Customer_Material_Detail = []
Install_Date = []
Source_Export = []

def getMaterial(material):
    for i in material:
        if i == "Non-Lead - Other":
            Material.append("Not Lead")
        elif i == "Non-Lead - Material Unknown":
            Material.append("Not Lead")
        elif i == "Non-Lead - Copper":
            Material.append("Not Lead")
        elif i == "Unknown - Material Unknown":
            Material.append("Unknown")

def getMaterialDetail(material,Material_Detail):
    for i in material:
        if i == "Non-Lead - Other":
            Material_Detail.append("Unknown")
        elif i == "Non-Lead - Material Unknown":
             Material_Detail.append("Unknown")
        elif i == "Non-Lead - Copper":
             Material_Detail.append("Copper")
        elif i == "Unknown - Material Unknown":
             Material_Detail.append("Unknown")

def getDate(date):
    for i in date:
        i = float(i)
        if i <1989:
            Install_Date.append("before July 1988")
        else:
            Install_Date.append("July 1988 or Newer")

def getCount(Install_Date):
    global Non_Lead
    global Unknowns
    Non_Lead = 0
    Unknowns = 0
    for i in Install_Date:
        if i == "July 1988 or Newer":
            Non_Lead += 1
        else:
            Unknowns += 1

def setRecords(Source):
    for i in Source:
        Source_Export.append("R = Records")

getMaterial(Utility_Material)
getDate(Utility_Install_Date)
getCount(Install_Date)
setRecords(Utility_Source)
getMaterialDetail(Utility_Material,Utility_Material_Detail)
getMaterialDetail(Customer_Material,Customer_Material_Detail)

print("Total Unknowns: ",Unknowns)
print("Total Non-Lead: ",Non_Lead)

data = {
    "Account Info": pd.Series(Account_ID), 
    "Physical Address": pd.Series(Address), 
    "Current Service Line Material - Distributor Size": pd.Series(Material), 
    "Verification Source - Distributor Side": pd.Series(Source_Export), 
    "Service Line Material Detail - Distributor Side": pd.Series(Utility_Material_Detail),
    "Service Line Installation Date - Distributor Side": pd.Series(Install_Date), 

    "Current Service Line Material - Consumer Side": pd.Series(Material),
    "Verification Source - Consumer Side": pd.Series(Source_Export),
    "Service Line Material Detail - Consumer Side": pd.Series(Customer_Material_Detail),
    "Service Line Installation Date - Consumer Side": pd.Series(Install_Date),

    "City": pd.Series(),
    "Location Data - Lat/Long (decimal degrees preferred)": pd.Series(),

    "Comments": pd.Series(Comments),
    "Occupancy Type": pd.Series(Occupancy_Type)
    }

df = pd.DataFrame(data)
df.to_csv(r"Z:\01305-0008\02-Engineering\03-Utilities\01_Service_Line_Inventory\Service_Line_Converter\output.csv")

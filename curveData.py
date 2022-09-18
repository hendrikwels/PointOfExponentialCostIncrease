import pandas as pd
import numpy as np
import xlwings as xw

# 1. Get User Input on Country, Market & Target Group
country = input("What's the Country? DE, AT or CH\n").lower()
market = country
if country == "ch":
    market = input("What's the Market? GCH or FCH\n").lower()  # only CH has 2 different Markets
core_target_group = input("What's your Target Group? Please use acronyms as 'TP20-49'\n").lower()
buying_target_group = input("What's your Buying Target Group? Please use acronyms as 'TP20-49'\n").lower()

# 2. Open Gross Contacts Calculator File
wb = xw.Book()
wb = xw.Book("160922_GrossContactsCalculatorTVFY2223.xlsm")
ws = wb.sheets["Manual TV"]  # ws is the worksheet object and the second Worksheet (Manual TV) in the Workbook



# 3. Select given User Input (Country, Market & Target Group)
def create_reach_data():
    ws.range("B3").value = country
    ws.range("D3").value = market
    ws.range("B6").value = core_target_group
    ws.range("C10").value = buying_target_group

    reach_curve_list = []

    for grp in range(10, 800, 10):  # only every 10th GRP until 800 Max
        ws.range("H10").value = grp
        current_reach = ws.range("H15").value
        reach_curve_list.append((grp, current_reach))

    # 4. Create a Pandas DataFrame from the reach_curve_list
    df = pd.DataFrame(reach_curve_list, columns=["GRP", "Reach"])

    # 5. Add a column with the Budget
    df["Budget"] = df["GRP"] * 1500 # 1500 EUR Proxy per GRP
    # #TODO: Create function to calculate average CPP

    # 6. Add a colum that calculated cost per Reach Point
    df["CostPerReachPoint"] = df["Budget"] / df["Reach"]

    # 7. transform the DataFrame into a CSV file
    df.to_csv("reach_curve.csv", index=False)

    return "reach_curve.csv"

    print(reach_curve_list)

    # Avoid opening a blank XLwings Workbook
    wb.close()

create_reach_data()

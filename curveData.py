import pandas as pd
import xlwings as xw
import tkinter as tk
from UserInterface import UserInterface

# Get User Input from UserInterface.py
my_UserInterface = UserInterface(tk.Tk())
my_UserInterface.window.mainloop()
user_input = my_UserInterface.user_input

# Define user Inputs
core_target_group = user_input["target_group"]
buying_target_group = user_input["buying_target_group"]
country = user_input["country"]
market = user_input["market"]
cpp = user_input["cpp"]


# 2. Open Gross Contacts Calculator File
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
    df["Budget"] = df["GRP"] * cpp

    # 6. Add a colum that calculated cost per Reach Point
    df["CostPerReachPoint"] = df["Budget"] / df["Reach"]

    # 7. transform the DataFrame into a CSV file
    df.to_csv("reach_curve.csv", index=False)

    # TODO: Avoid opening a Blank Excel File
    wb.close()
    return "reach_curve.csv"
    # TODO: Provide User with CSV File to download

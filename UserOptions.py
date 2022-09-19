import xlwings as xw
import pandas as pd

# Make a List of all possible Target Group Options

# Open Excel File
wb = xw.Book()
wb = xw.Book("160922_GrossContactsCalculatorTVFY2223.xlsm")
ws = wb.sheets["Lookup"]  # ws is the worksheet object

# Turn Sheet into a CSV File avoid skipping the first column
ws.range("A1").options(pd.DataFrame, expand='table').value.to_csv("target_group_list.csv")

# Turn the CSV File into a Pandas DataFrame
df = pd.read_csv("target_group_list.csv")

# Rename Columns to make them more readable
df.rename(columns={'M arket': 'Market', 'DeM o': 'DemoTG'}, inplace=True)

# Create an empty List to store the Target Group Options
target_group_list = []
print(df) # checking for Errors and NaN Values

# Create a loop that iterates through the Target Group Options in the Excel File
# Only loop through the Cells that match "FY 22/23" in Column A
for index, cell in enumerate(df["FY"]):
    if cell == "FY 22/23":
        target_group_list.append(df.iloc[index, 4]) # 4th column is DemoTG
    else:
        pass

# remove the NaN Values from the List
target_group_list = [x for x in target_group_list if str(x) != 'nan']

# Transform the List into a Set to remove duplicates
target_group_list = set(target_group_list)
# Transform the Set back into a List
target_group_list = list(target_group_list)

# Export the List into a separate python file
with open("target_group_list.py", "w") as f:
    f.write("target_group_list = ")
    f.write(str(target_group_list))
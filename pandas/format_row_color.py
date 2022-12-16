#You can use this code to sort a csv by column, and highlight rows by those column values

import pandas as pd
import openpyxl

# Load the kb4 csv into a dataframe
df = pd.read_csv("file.csv")

# Specify which columns to keep in the dataframe
df = df[['col1', 'col2', 'col3']]

# Sort the columns based on passed etc..
df = df.sort_values('col3', ascending=True)

# Define a function to change the colors based on the Status column
def highlight_rows(s):
    con = s.copy()
    con[:] = None
    if (s['col3'] == 'string for color1'):
        con[:] = "background-color: green"
    elif (s['col3'] == 'string for color2'):
        con[:] = "background-color: red"
    elif (s['col3'] == 'string for color3'):
        con[:] = "background-color: yellow"
    return con

# Apply the style to the Status column
df = df.style.apply(highlight_rows, axis=1)

# Export the formatted dataframe to Excel
df.to_excel("formatted.xlsx", index=False)

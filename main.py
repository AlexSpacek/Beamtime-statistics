import numpy as np
import pandas as pd
from IPython.display import display

#load data from excel: all sheets into df1 dictionary whose keys are sheet names
xlsx = pd.ExcelFile('L1_hour_count.xlsx')
df1 = pd.read_excel(xlsx, None)
display(df1["2022"])
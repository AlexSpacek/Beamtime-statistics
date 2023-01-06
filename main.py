import pandas as pd
from cleaner import yearly_sheet
from plotMethods import yearly_histogram_total_hours,average_hours_per_day,yearly_histogram_net_hours,average_net_beamtime_per_day,yearly_whole_weeks,yearly_whole_days_per_week,yearly_power_leve_pie



xlsx = pd.ExcelFile('L1_hour_count.xlsx')
dict1 = pd.read_excel(xlsx, None)

#Loop iterates over sheet names that correspond to a year number, the data is clean and stored in the yearly_sheet class...
# data[] then stores these objects in a dictionary with year numbers as keys
data={} 
for keys in dict1.keys():
    try:
        if keys!='Template':
            data[keys]=yearly_sheet(float(keys),dict1[keys])
    except:
        print("One sheet with unexpected name")
        

yearly_power_leve_pie(data)
yearly_histogram_total_hours(data)
average_hours_per_day(data)
yearly_histogram_net_hours(data)
average_net_beamtime_per_day(data)
yearly_whole_weeks(data)
yearly_whole_days_per_week(data)


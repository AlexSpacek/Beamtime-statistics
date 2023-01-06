#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import modules
import pandas as pd
from cleaner import yearly_sheet
from plotMethods import yearly_histogram_total_hours,average_hours_per_day,yearly_histogram_net_hours,average_net_beamtime_per_day,yearly_whole_weeks,yearly_whole_days_per_week,yearly_power_leve_pie


# In[2]:


#load data from excel: all sheets into df1 dictionary whose keys are sheet names
xlsx = pd.ExcelFile('L1_hour_count.xlsx')
dict1 = pd.read_excel(xlsx, None)


# In[3]:


#Loop iterates over sheet names that correspond to a year number, the data is clean and stored in the yearly_sheet class...
# data[] then stores these objects in a dictionary with year numbers as keys
data={} 
for keys in dict1.keys():
    try:
        if keys!='Template':
            data[keys]=yearly_sheet(float(keys),dict1[keys])
    except:
        print("One sheet with unexpected name")
        


# In[4]:


yearly_power_leve_pie(data)


# In[5]:


yearly_histogram_total_hours(data)
average_hours_per_day(data)


# In[6]:



yearly_histogram_net_hours(data)
average_net_beamtime_per_day(data)


# In[7]:


yearly_whole_weeks(data)
yearly_whole_days_per_week(data)


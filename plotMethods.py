#Function for plotting the various statistics for beamtime analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def yearly_histogram_total_hours(data):
    totalHours = np.array([])
    for key in data:
        totalHours = np.append(totalHours, np.sum(data[key].sheet['Total Time (Including standby)']))
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    students = [23,17,35,29,12]
    ax.bar(years,totalHours)
    ax.set_ylabel("Time [h]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Total beamtime per year (including standby)", fontsize=18)
    plt.savefig('total_hours.png',bbox_inches='tight')
    return 
def average_hours_per_day(data):
    totalHours = np.array([])
    for key in data:
        totalHours = np.append(totalHours, np.sum(data[key].sheet['Total Time (Including standby)'])/len(data[key].sheet['Total Time (Including standby)']))
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    students = [23,17,35,29,12]
    ax.bar(years,totalHours)
    ax.set_ylabel("Time [h]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Average beamtime per day (including standby)", fontsize=18)
    plt.savefig('total_hours_per_day.png',bbox_inches='tight')
    return 
def yearly_histogram_net_hours(data):
    totalHours = np.array([])
    for key in data:
        totalHours = np.append(totalHours, np.sum(data[key].sheet['Net Beamtime']))
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    students = [23,17,35,29,12]
    ax.bar(years,totalHours)
    ax.set_ylabel("Time [h]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Net beamtime per year", fontsize=18)
    plt.savefig('net_hours.png',bbox_inches='tight')
    return 
def average_net_beamtime_per_day(data):
    totalHours = np.array([])
    for key in data:
        totalHours = np.append(totalHours, np.sum(data[key].sheet['Net Beamtime'])/len(data[key].sheet['Net Beamtime']))
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    students = [23,17,35,29,12]
    ax.bar(years,totalHours)
    ax.set_ylabel("Time [h]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Average net beamtime per day", fontsize=18)
    plt.savefig('net_hours_per_day.png',bbox_inches='tight')
    return     
def yearly_whole_days(data):
    totalHours = np.array([])
    for key in data:
        newFrame=np.array(data[key].sheet[['8-9','9-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22','22-23']].fillna(-1), dtype=np.int64)
        Ndays = np.array([])
        for row in newFrame:
            if np.sum([row>-1])<4:
                Ndays = np.append(Ndays,0)
            elif np.sum([row>-1])>3 and np.sum([row[11:14]>-1])>0:   
                Ndays = np.append(Ndays,1.5)
            else:
                Ndays = np.append(Ndays,1)    
        totalHours = np.append(totalHours, np.sum(Ndays))        
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    students = [23,17,35,29,12]
    ax.bar(years,totalHours)
    ax.set_ylabel("Number of days [-]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Beam days per year (1day>4h and 1.5day if >19h)", fontsize=18)
    plt.savefig('total_beam_days.png',bbox_inches='tight')
    return         
def yearly_whole_days_per_day(data):
    totalHours = np.array([])
    for key in data:
        newFrame=np.array(data[key].sheet[['8-9','9-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22','22-23']].fillna(-1), dtype=np.int64)
        Ndays = np.array([])
        for row in newFrame:
            if np.sum([row>-1])<4:
                Ndays = np.append(Ndays,0)
            elif np.sum([row>-1])>3 and np.sum([row[11:14]>-1])>0:   
                Ndays = np.append(Ndays,1.5)
            else:
                Ndays = np.append(Ndays,1)  
        totalHours = np.append(totalHours, np.sum(Ndays)/len(Ndays))        
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    students = [23,17,35,29,12]
    ax.bar(years,totalHours)
    ax.set_ylabel("Number of days [-]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Average beam days per day (1day>4h and 1.5day if >19h)", fontsize=18)
    plt.savefig('total_beam_days_per_day.png',bbox_inches='tight')
    return         
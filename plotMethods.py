#Function for plotting the various statistics for beamtime analysis
import numpy as np
import matplotlib.pyplot as plt

def yearly_histogram_total_hours(data):
    totalHours = np.array([])
    for key in data:
        totalHours = np.append(totalHours, np.sum(data[key].sheet['Total Time (Including standby)']))
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    ax.bar(years,totalHours)
    ax.set_ylabel("Time [h]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Total beamtime per year (including standby)", fontsize=16,fontweight="bold", pad=22)
    plt.setp(ax.get_xticklabels(), fontsize=14)
    plt.setp(ax.get_yticklabels(), fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Make some labels.
    rects = ax.patches
    totalHours=totalHours.round(decimals=1)
    labels = totalHours.tolist()
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
                ha='center', va='bottom', size=14, fontdict=None)

    plt.savefig('Figures/total_hours.png',bbox_inches='tight')
    return 
def average_hours_per_day(data):
    totalHours = np.array([])
    for key in data:
        totalHours = np.append(totalHours, np.sum(data[key].sheet['Total Time (Including standby)'])/len(data[key].sheet['Total Time (Including standby)']))
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    ax.bar(years,totalHours)
    ax.set_ylabel("Time [h]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Average beamtime per day (including standby)", fontsize=16,fontweight="bold", pad=22)
    plt.setp(ax.get_xticklabels(), fontsize=14)
    plt.setp(ax.get_yticklabels(), fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Make some labels.
    rects = ax.patches
    totalHours=totalHours.round(decimals=1)
    labels = totalHours.tolist()
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
                ha='center', va='bottom', size=14, fontdict=None)

    plt.savefig('Figures/total_hours_per_day.png',bbox_inches='tight')
    return 
def yearly_histogram_net_hours(data):
    totalHours = np.array([])
    for key in data:
        totalHours = np.append(totalHours, np.sum(data[key].sheet['Net Beamtime']))
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    ax.bar(years,totalHours)
    ax.set_ylabel("Time [h]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Net beamtime per year", fontsize=16,fontweight="bold", pad=22)
    plt.setp(ax.get_xticklabels(), fontsize=14)
    plt.setp(ax.get_yticklabels(), fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Make some labels.
    rects = ax.patches
    totalHours=totalHours.round(decimals=1)
    labels = totalHours.tolist()
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
                ha='center', va='bottom', size=14, fontdict=None)

    plt.savefig('net_hours.png',bbox_inches='tight')
    return 
def average_net_beamtime_per_day(data):
    totalHours = np.array([])
    for key in data:
        totalHours = np.append(totalHours, np.sum(data[key].sheet['Net Beamtime'])/len(data[key].sheet['Net Beamtime']))
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    ax.bar(years,totalHours)
    ax.set_ylabel("Time [h]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Average net beamtime per day", fontsize=16,fontweight="bold", pad=22)
    plt.setp(ax.get_xticklabels(), fontsize=14)
    plt.setp(ax.get_yticklabels(), fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Make some labels.
    rects = ax.patches
    totalHours=totalHours.round(decimals=1)
    labels = totalHours.tolist()
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
                ha='center', va='bottom', size=14, fontdict=None)

    plt.savefig('Figures/net_hours_per_day.png',bbox_inches='tight')
    return     
def yearly_whole_weeks(data):
    totalHours = np.array([])
    for key in data:
        newFrame=np.array(data[key].sheet[['8-9','9-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22','22-23','23-24']].fillna(-1), dtype=np.int64)
        Ndays = np.array([])
        for row in newFrame:
            if np.sum([row>-1])<4:
                Ndays = np.append(Ndays,0)
            elif np.sum([row>-1])>3 and np.sum([row[11:15]>-1])>0:   
                Ndays = np.append(Ndays,1.5)
            else:
                Ndays = np.append(Ndays,1)    
        totalHours = np.append(totalHours, np.sum(Ndays)/5)        
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    ax.bar(years,totalHours)
    ax.set_ylabel("Number of weeks [-]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Beam weeks per year (1day>4h and 1.5day if past 19:00)", fontsize=16,fontweight="bold", pad=22)
    plt.setp(ax.get_xticklabels(), fontsize=14)
    plt.setp(ax.get_yticklabels(), fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Make some labels.
    rects = ax.patches
    totalHours=totalHours.round(decimals=1)
    labels = totalHours.tolist()
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
                ha='center', va='bottom', size=14, fontdict=None)

    plt.savefig('Figures/total_beam_weeks.png',bbox_inches='tight')
    return         
def yearly_whole_days_per_week(data):
    totalHours = np.array([])
    for key in data:
        newFrame=np.array(data[key].sheet[['8-9','9-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22','22-23','23-24']].fillna(-1), dtype=np.int64)
        Ndays = np.array([])
        for row in newFrame:
            if np.sum([row>-1])<4:
                Ndays = np.append(Ndays,0)
            elif np.sum([row>-1])>3 and np.sum([row[11:15]>-1])>0:   
                Ndays = np.append(Ndays,1.5)
            else:
                Ndays = np.append(Ndays,1)  
        totalHours = np.append(totalHours, np.sum(Ndays)/(len(Ndays)/5))        
    fig = plt.figure(facecolor=(1, 1, 1))
    ax = fig.add_axes([0,0,1,1])
    years = list(data.keys())
    ax.bar(years,totalHours)
    ax.set_ylabel("Number of days [-]", fontsize=14)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_title("Average beam days per week (1day>4h and 1.5day if past 19:00)", fontsize=16,fontweight="bold", pad=22)
    plt.setp(ax.get_xticklabels(), fontsize=14)
    plt.setp(ax.get_yticklabels(), fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Make some labels.
    rects = ax.patches
    totalHours=totalHours.round(decimals=1)
    labels = totalHours.tolist()
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
                ha='center', va='bottom', size=14, fontdict=None)
  
    plt.savefig('Figures/total_beam_days_per_week.png',bbox_inches='tight')
    return         
def yearly_power_leve_pie(data):
    totalHours = np.array([])
    fig = plt.figure(figsize=(25,10))
    i= [0,3,4,5,6,7] #this is the feature I used
    r,c = 0 ,0   #these are the rows(r) and columns(c)
    theme = plt.get_cmap('hsv')
    labels=['Power Level 7','Power Level 6','Power Level 5','Power Level 4','Power Level 3','Standby']
    for key in data:
        newFrame=np.array(data[key].sheet[['8-9','9-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22','22-23','23-24']].fillna(-1), dtype=np.int64)
        standby=np.count_nonzero(newFrame==0)
        PL1=np.count_nonzero(newFrame==3)
        PL2=np.count_nonzero(newFrame==4)
        PL3=np.count_nonzero(newFrame==5)
        PL4=np.count_nonzero(newFrame==6)
        PL5=np.count_nonzero(newFrame==7)  
        if c < 3:
            #weekday
            ax1 = plt.subplot2grid((2,3), (r, c))
            ax1.set_prop_cycle("color", [theme(1. * i / 6)
                             for i in range(6)])
            plt.pie([PL5,PL4,PL3,PL2,PL1,standby])
            plt.legend(labels,bbox_to_anchor=(1,0.5), loc="center right", fontsize=18, 
            bbox_transform=plt.gcf().transFigure) 
            plt.title(key,fontsize=18)
            # plt.title(feature[i])
            c +=1 #go one column to the left
        else:
            c = 0 #reset column number as we exceeded 4 columns
            r = 1 #go into the second row
            ax1 = plt.subplot2grid((2,3), (r, c))
            ax1.set_prop_cycle("color", [theme(1. * i / 6)
                             for i in range(6)])
            plt.pie([PL5,PL4,PL3,PL2,PL1,standby])
            plt.legend(labels,bbox_to_anchor=(1,0.5), loc="center right", fontsize=18, 
            bbox_transform=plt.gcf().transFigure) 
            plt.title(key,fontsize=18)
            # plt.title(days[i])
            c +=1
     #,dpi=1600)
    
    plt.savefig('Figures/Power_levels.png',dpi=300)
    return             
   
#Object holding the data of one year of beamtime and various cleaning/sorting methods for the data
# import pandas as pd

class yearly_sheet():
    # CONSTRUCTOR
    def __init__(self, year, sheet):
        # save the name of the sheet ...represently the year of operation
        self.year = year
        self.sheet = sheet
        self.selectUserRuns()
        self.properColumnNames()
    # METHODS
    def selectUserRuns(self):
        #select days of user runs based on the date column
        self.sheet = self.sheet[self.sheet.iloc[:,1].notna()]
        return 
    def properColumnNames(self):
        #properly label columns, year 2019 is an exception which lacks Requested Hours label
        if self.year>2019:
            self.sheet=self.sheet.set_axis(['Month','Date','Operators','8-9','9-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22','22-23','23-24','Net Beamtime','Total Time (Including standby)','Requested hours','Notes1','Notes2','Notes3','Notes4'], axis=1)
        else:
            self.sheet=self.sheet.set_axis(['Month','Date','Operators','8-9','9-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22','22-23','23-24','Net Beamtime','Total Time (Including standby)','Notes1','Notes2','Notes3','Notes4'], axis=1)        
        #the first row should be discarded as it is the original column names
        if self.year==2019 or self.year==2020:
            self.sheet=self.sheet.iloc[1: , :]
        return
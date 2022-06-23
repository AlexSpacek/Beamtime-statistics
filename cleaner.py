#Object holding the data of one year of beamtime and various cleaning/sorting methods for the data
import pandas as pd

class yearly_sheet():
    # CONSTRUCTOR
    def __init__(self, year, sheet):
        # save the name of the sheet ...represently the year of operation
        self.year = year
        self.sheet = self.cleaner(sheet)
        return
    # METHODS
    def cleaner(self,sheet):
        #select days of user runs based on the date column
        cleanedSheet=self.selectUserRuns(sheet)
        return cleanedSheet
    def selectUserRuns(self,sheet):
        #select days of user runs based on the date column
        userRuns = sheet[sheet.iloc[:,1].notna()]
        return userRuns
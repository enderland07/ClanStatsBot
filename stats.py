import numpy as np
import json

from API import API
from data import Data

class Stats():
    def __init__(self):
        print("works")

    expectedDmg = 12975.9242622
    expectedWR = 47.8895036
    expectedWins = 0
    expectedKills = 0.535497704918

    def calculatePR(self,dmg,kills,WR): #player): #player is an object of Player()
        

        #self.expectedWins = (self.expectedWR/100)*self.Battles

        #print(self.expectedWins)

        rDmg = dmg/self.expectedDmg
        rWR = WR/self.expectedWR
        rKills = kills/self.expectedKills

        nDmg = max(0,(rDmg-0.4)/(1-0.4))
        nWR = max(0,(rWR-0.7)/(1-0.7))
        nKills = max(0,(rKills-0.1)/(1-0.1))

        return (700*nDmg + 300*nKills + 150*nWR)

    def saveExpValues(self):
        dt = Data('test')
        api = API()

        temp = api.expectedValues()
        time = temp['time']

        for shipid,shipdata in temp['data'].items():
            print(shipid)
            for key in shipdata:
                print(shipdata[key])
            
        print(time)
        return temp['data']

if(__name__=="__main__"):
    #a = float(input("dmg: "))
    #b = float(input("kills: "))
    #c = float(input("wr: "))
    #d = Stats()
    #print(d.calculatePR(a,b,c))
    d = Stats()
    d.saveExpValues()

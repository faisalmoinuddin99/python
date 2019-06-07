#!/usr/bin/python3
from inherit import Bike

#Exercise files by IgneusTech.COM
class Harley(Bike):
    def __init__(self, **kwargs):
        self.features = kwargs
    
    def bigEngine(self):
        print("Harley got a big Engine", self._cc)
        
    def loudSound(self):
        print("Potato sound is really cool", self._cc)
        
    def setFeatures(self, k, v):
        self.features[k] = v
        
    def getFeatures(self, k):
        return self.features.get(k, None)
    
    def seat(self):
        super().seat()
        print("Got a Harley seat")
     
        




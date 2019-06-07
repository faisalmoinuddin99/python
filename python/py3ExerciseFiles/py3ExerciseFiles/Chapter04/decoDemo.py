#!/usr/bin/python3

#Exercise files by IgneusTech.COM
class Harley():
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
     
    @property
    def topSpeed(self):
        return self.features.get('topSpeed', None)
    
    @topSpeed.setter
    def topSpeed(self, ts):
        self.features['topSpeed'] = ts
        
    @topSpeed.deleter
    def topSpeed(self):
        del self.features['topSpeed']
         
     
     
def main():
    print("Hello")
    
    streetBob = Harley()
    streetBob.setFeatures('cc', '1800')
    print(streetBob.getFeatures('cc'))
    
    streetBob.topSpeed = 300
    
if __name__ == "__main__":  main()        




#!/usr/bin/python3

#Exercise files by IgneusTech.COM
from classDemo import Harley

def main():
    print("Hello")
    
    streetBob = Harley()
    streetBob.setFeatures('cc', '1800')
    print(streetBob.getFeatures('cc'))
    
    streetBob.setFeatures('hp', '45')
    print(streetBob.getFeatures('hp'))
    
    streetBob.setFeatures('color', 'orange')
    print(streetBob.getFeatures('color'))
    
    fatbob = Harley()
    fatbob.setFeatures('cc', '2000')
    print(fatbob.getFeatures('cc'))
    
    fatbob.setFeatures('hp', '85')
    print(fatbob.getFeatures('hp'))
    
    fatbob.setFeatures('color', 'Blue')
    print(fatbob.getFeatures('color'))
    fatbob.seat()
    
    
    
    
#     streetBob._cc = 750
#     print(streetBob._cc)
#     streetBob.loudSound()
#     streetBob.bigEngine()
#     
#     fatboy = Harley(1800)
#     fatboy.bigEngine()
    
    
if __name__ == "__main__":  main()





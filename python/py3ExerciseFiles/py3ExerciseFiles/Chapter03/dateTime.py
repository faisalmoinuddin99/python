#!/usr/bin/python3
from datetime import date


#Exercise files by IgneusTech.COM
def main():
    print("Hello")
    
    currentDate = date.today()
    print(currentDate)
    
    print("day is ", currentDate.day)
    print("Month is ", currentDate.month)
    print("Year is ", currentDate.year)
    print("Weekday is ", currentDate.weekday())
    
    
       
    
    
if __name__ == "__main__":  main()
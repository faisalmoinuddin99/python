#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    days = dict(
                one = "Monday",
                two = "Tuesday",
                three = "Wednesday"

                )
    
    day = "three"
    print(days.get(day, 'No match'))


if __name__ == "__main__":  main()
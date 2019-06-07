#!/usr/bin/python3

#Exercise files by IgneusTech.COM
from _codecs import encode
import re
import urllib.request


def main():
    print("Hello")
    
    web = urllib.request.urlopen('https://www.python.org/')
    for code in web:
        print(str(code, encoding = 'utf_8'), end = ' ')

    #assignment time
    
    
if __name__ == "__main__":  main()





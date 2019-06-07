#!/usr/bin/python3

#Exercise files by IgneusTech.COM
import re

def main():
    print("Hello")
    
    file = open("google.txt")
    
    for i in file:
        print( re.sub('(G|g)oogle', '*******', i), end=' ')
    
if __name__ == "__main__":  main()





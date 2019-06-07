#!/usr/bin/python3

#Exercise files by IgneusTech.COM
import re

def main():
    print("Hello")
    
    file = open("google.txt")
    
    for i in file:
        patternMatch = re.search("(G|g)oogle", i)
        if patternMatch:
            print(patternMatch.group())
    
if __name__ == "__main__":  main()





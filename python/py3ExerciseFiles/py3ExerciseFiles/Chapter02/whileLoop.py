#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    first = 0
    second = 1
    print(first)
    while second < 200:
        print(second, end=' ')
        first, second = second, first + second
       

if __name__ == "__main__":  main()
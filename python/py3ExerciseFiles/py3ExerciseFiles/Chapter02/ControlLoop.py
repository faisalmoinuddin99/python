#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    msg = "Welcome to the Python Course"
    
    for c in msg:
        if c == 'n':
            continue
        print(c, end=' ')
    print("\nI am out of the loop")
if __name__ == "__main__":  main()
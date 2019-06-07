#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    lower = "i am a string"
    upper = "I AM A STRING"
    cash = 20
    
    print(lower.upper())
    print(upper.lower())
    print(upper.capitalize())
    newString = upper.swapcase()
    print(id(upper), "and new is", id(newString))
    print("i am a string too".upper())
    print("I got a {} $ cash".format(cash))
    
    print(lower.find('am'))
    print(lower.replace('am', 'will be'))
    
    
    userInput1 = "  I am a input    "
    userInput2 = "   I am input 2"
    userInput3 = "I am input 3    "
    userInput4 = "  I am input 4"
    
    
    
    print(userInput1.strip())
    print(userInput2.strip())
    print(userInput3.rstrip())
    print(userInput4.split(sep=None))
    
    
    
    sysInput = "iamastring"
    sysInput2 = "23223"
    
    print(sysInput.isalnum())
    print(userInput1.isalnum())
    print(sysInput2.isdigit())
    
if __name__ == "__main__":  main()
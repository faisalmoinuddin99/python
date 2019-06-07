#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    myFunc(3020, 21)
    yourFunc(1,2,3,4, 5, 6, 7)
    
def myFunc(pin, age = None):
    if age is None:
        print("He is allowed in party")
    print("My pin is {} and age is {} ".format(pin, age) )
    
    #multiple argument Movie
    
def yourFunc(one, two, *args):
    print("the values are {}, {}, {}".format(one, two, args) )  
    #for i in args: print(args)
    
    
    #KWArgs or known as Key Word Arguments
    ourFunc(1, 2, 3, 4, 5, 6 , onee = "Monday", twoo = "Tuesday")
    
def ourFunc(a, b, c, *args, **kwargs):
    print("hello", kwargs['onee'], kwargs['twoo'])
    
    # Return in function
    print(returnFunc())
    for i in returnFunc(): print(i, end="-")
def returnFunc():
    #return range(10)
    return "Hello World"
    
if __name__ == "__main__":  main()





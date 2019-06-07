#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    di = dict(one = 1, two = 2, three = 3, four = 4)
    print(type(di))
    
    ei = dict(five = 5, six = 6)
    print(ei['six'])
    
    fi = dict(zero=0, **di)
    print(fi)      
    
    print('one' in fi)
    
    for key in fi:
        print(key)
        
    print('****************')
    
    for key, val in fi.items():
        print(key, val)
        
    print(fi.get('two', 'NO match'))
    
if __name__ == "__main__":  main()
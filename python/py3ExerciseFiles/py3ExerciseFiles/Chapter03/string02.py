#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    no1 = 4
    no2 = 5
    
    print('Value one is {1} and value two is {0}'.format(no1, no2))
    
    str1 = "top ten programming language in 2016"
    u = str1.split()
    print(u)
    
    for i in u:
        print(i, end='-')
     
    print('\n')      
    url = '-'.join(u)
    print(url,".html")      
    
    
if __name__ == "__main__":  main()
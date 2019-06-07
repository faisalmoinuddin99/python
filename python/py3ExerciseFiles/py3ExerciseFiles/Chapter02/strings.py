#!/usr/bin/python3

#Exercise files by IgneusTech.COM
'''
this is
a multi line
comment

'''
def main():
    
    balance = 90
    number = 80
    str1 = 'This is \n one string'
    str2 = r"This is {} two {} string".format(balance, number)
    str3 = '''\
    This is 
    third string '''
    str4 = """ THis is fourth string """
    
    
    print(str2)

if __name__ == "__main__":  main()
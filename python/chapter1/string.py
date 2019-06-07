def string():
    balance = 90
    number = 89
    str1 = 'this \n is string one'
    str2 = "this is string two"
    str3 = '''
    this
    is string three '''
    str4 = """ this is {} string {} four """.format(balance,number)
    print(str4)
if __name__ == '__main__':string()

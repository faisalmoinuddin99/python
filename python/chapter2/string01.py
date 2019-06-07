def main():
    lower = 'i am string'
    upper = 'I AM STRING'
    cash = 20
    print(lower.upper())
    print(upper.lower())
    print('i got a cash of {}'.format(cash))
    print(lower.find('am'))
    print(lower.replace('am','will be'))

    userinput1 = '    i am input     '
    userinput2 = 'i am input      '
    userinput3 = 'I am input '
    userinput4 = 'I am input'


    print(userinput1.strip())
    print(userinput2.strip())
    print(userinput4.split(sep=None))
    print(userinput3.rstrip())
if __name__ == '__main__':main()

def __main__():
    tuple = (2,5,6)
    #tuples are fixed
    print(tuple)

    #List
    list = [4,1,9,3,2,0,45]
    list.sort()
    print(list)

    #Dictionary

    dict1 = {'one':1,'two':2}
    print(dict1)
    dict2 = dict([('one',1),('two',2)])
    print(dict2)
    dict3 = dict(one=1,two=2)
    print(dict3)

    #Python | Merging two Dictionaries

    dictA = dict(one=1,two=2)
    dictB = dict(goku=4000)
    dictC = dictA.update(dictB)
    print(dictA)

    #Python Exercise: Check if a given key already exists in a dictionary
    d = dict(one=1,two=2,five=5,three=3)
    def __ispresent__(x):
        if x in d:
            print('already exists')
        else:
            print('not found')
        __ispresent__(5)
        __ispresent__(2)
    if __name__ == '__main__':__ispresent__()


if __name__ == '__main__':__main__()

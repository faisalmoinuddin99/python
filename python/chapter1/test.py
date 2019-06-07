def test():
    dict = {0: 10, 1: 20}
    print(dict)
    dict['2'] = 30
    dict['geek'] = 'for'
    print("updated",dict)



if __name__ == '__main__':test()

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(2)







def vovals():
    x ='v'
    if x == 'a' or x == 'e' or x =='i' or x == 'o' or x == 'u':
        print('vovals')
    else:
        print('conconant')
if __name__ == '__main__':vovals()


def dbs():
    dbs = dict(
    one = 'goku',
    two = 'vegeta',
    )
    fighter = 'three'
    print(dbs.get(fighter,'no match'))

if __name__ == '__main__': dbs()

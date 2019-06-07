
#fibonnaci series
def fib():
    first = 0
    second = 1
    print(first, end=' ')
    while second < 100:
        print(second,end=' ')
        first ,second = second,first+second


if __name__ == '__main__':fib()

#factorial program

def fact():
    num = 5
    fact = 1
    while num > 0:
        print(fact)
        fact = fact * num
        num = num - 1


if __name__ == '__main__':fact()


def __main__():
    value = [10,20,30]
    while value:
        print(value.pop())

if __name__ == '__main__':__main__()

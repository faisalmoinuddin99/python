#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    tupy = 1,2,3,4,5
    print(tupy)
    
    singleTupy = (1,)
    print(type(singleTupy))
    
    tupo = tuple(range(20))  #Fixed
    listo = list(range(21,41))  #change this
    
    print(2 in tupo)
    
    
    listo.append(200)
    print(listo)

    
    
if __name__ == "__main__":  main()
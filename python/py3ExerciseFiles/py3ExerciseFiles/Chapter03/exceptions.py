#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    #Open a file in read mode
    
    try:
        file = open("file.doc")
        for text in file:
            print(text, end="")
     
    except IOError as msg : 
        print("file not found", msg)
     
        
    print("\ngood line")
    
if __name__ == "__main__":  main()





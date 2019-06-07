#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
    buff = 60000
    newFile = open("fb.jpg", "rb")
    outputFile = open("fbnew.jpg", "wb")
    
    buffer = newFile.read(buff)
    while len(buffer):
        outputFile.write(buffer)
        buffer = newFile.read(buff)
        
    print("\nDone")
        
        
        
    
    
    
if __name__ == "__main__":  main()
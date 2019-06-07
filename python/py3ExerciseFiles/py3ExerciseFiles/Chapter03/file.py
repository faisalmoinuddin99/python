#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    #Open a file in read mode
#     file = open("file.txt")
#     
#     for text in file:
#         print(text, end="")
#     
    #Create a new file from existing file
    newfile = open("file.txt")
    outputFile = open("Myfile.txt", 'w')
    
    for text in newfile:
        print(text, file = outputFile, end="")
        
    print("Work Done Boss!")
    
    
if __name__ == "__main__":  main()





#!/usr/bin/python3

#This is an exercise file

def main(): 
    ScoreKevin = 500
    defaultHighScore = 100
#     
#     if ScoreKevin > defaultHighScore:
#         print("Kevin you did that, congrats")
#         
#     elif ScoreKevin < defaultHighScore: 
#         print("Try harder Kevin")
#         
#     else:
#         print("Score equals to the default score") 
#     

    msg = "you did it" if ScoreKevin > defaultHighScore else "you didn't made it"
    print(msg)
    
    
    #print("Hello world")
     
if __name__ == "__main__":  main()
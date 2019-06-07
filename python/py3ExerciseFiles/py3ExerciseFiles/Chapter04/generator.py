#!/usr/bin/python3

#Exercise files by IgneusTech.COM

def main():
    print("Hello")
    
# def squareList(nums):
#     for i in nums:
#         yield (i*i)
#     

#myNums = squareList([1,2,3,4,5])
myNums = [x*x for x in [1,2,3,4,5]]

print(myNums) #[1,4,9,16,25]
# print(next(myNums))
# print(next(myNums))
# print(next(myNums))
# print(next(myNums))

# for i in myNums:
#     print(i)

    
if __name__ == "__main__":  main()





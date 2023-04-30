myList = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(myList)):
    if i%2 == 0:
        print(myList[i])
print("Another program")
n = int(input("Enter a number(to repeat the following series till that number):"))
for i in range(1,n+1):
    print(i**2, end=",")
    
int_list = [1, 2, 3, 4, 5, 6]
sum = 0
for iter in int_list:
    sum = sum + iter
print("Sum =", sum)
print("Avg =", sum/len(int_list))
myList = [12,24,56,78,]
myList.append([45,65])
myList.extend([86,97])
print(myList)
list1 = [12,24,45,65,86,90,10]
list1.sort()
print(list1)
list2 = [12,45,57,37,86,49]
sorted(list2)
print(list2)
list3 =[11,22,33,44,55,66,77,88,99,10]
list3[::-2]
list3[:3] + list3[3:]
print(list3)
list4 = [17,23,34,42,59,67,73,12,10]
list4[len(list4)-1] 
print(list4)
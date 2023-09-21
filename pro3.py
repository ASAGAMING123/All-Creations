n = [999999,99,89,79,56,66,998]
sum = 0
val = 0
while val < len(n):
    sum = sum + n[val]
    val+=1
print(f"The sum of the given list is {sum}.")
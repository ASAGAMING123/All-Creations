list = [1,5,7,8,9]
sum = sum(list)
Number = len(list)
Average = sum/Number
print(f"Average of the following numbers is {Average}.")
sideA = float(input("Enter the first side:"))
sideB = float(input("Enter the second side:"))
sideC = float(input("Enter the third side:"))
s = (sideA+sideB+sideC)/2
area = s*(s-sideA)*(s-sideB)*(s-sideC)
ans = area**(1/2)
print(f"Area of triangle with sides {sideA}m,{sideB}m and {sideC}m is {ans}m².")
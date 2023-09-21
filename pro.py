x = float(input("Enter a 1st no.:"))
y = float(input("Enter a 2nd no.:"))
z = float(input("Enter a 3rd no.:"))
if x > y  and x > z:
    print(f"The greatest no. is {x}.")
elif y > x  and y > z:
    print(f"The greatest no. is {y}.")
else:
    print(f"The greatest no. is {z}.")
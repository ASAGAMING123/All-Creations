num_1 = float(input("Enter a number:"))
operator = str(input("Enter the operator:"))
num_2 = float(input("Enter a number:"))
if operator == "+":
 num_3 = num_1 + num_2
 print(f"The result is {num_3}.")
elif operator == "-":
 num_3 = num_1 - num_2
 print(f"The result is {num_3}.")
elif operator == "*":
 num_3 = num_1 * num_2
 print(f"The result is {num_3}.")
elif operator == "/":
 num_3 = num_1 / num_2
 print(f"The result is {num_3}.")
elif operator == "^":
 num_3 = num_1 ** num_2
 print(f"The result is {num_3}.")
elif operator == "|":
 num_3 = num_1 ** (1/num_2)
 print(f"The result is {num_3}.")
elif operator == "%":
 num_3 = (num_1/100) * num_2
 print(f"The result is {num_3}.")
else:
 print("Invalid operator.")
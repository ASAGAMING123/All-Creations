while True:
 num_1 = eval(input("Enter a number:"))
 operator = str(input("Enter the operator:"))
 num_2 = eval(input("Enter a number:"))
 if operator == "+":
  num_3 = num_1 + num_2
  print(num_1,operator,num_2,"=",num_3,"\n")
 elif operator == "-":
  num_3 = num_1 - num_2
  print(num_1,operator,num_2,"=",num_3,"\n")
 elif operator == "*" or operator == "x":
  num_3 = num_1 * num_2
  print(num_1,operator,num_2,"=",num_3,"\n")
 elif operator == "/":
  if num_2==0:
   print(num_1,operator,num_2,"= Infinity","\n")
  else:
   num_3 = num_1 / num_2
   print(num_1,operator,num_2,"=",num_3,"\n")
 elif operator == "^":
  num_3 = num_1 ** num_2
  print(num_1,operator,num_2,"=",num_3,"\n")
 elif operator == "|":
  if num_2==0:
   print(num_1,operator,num_2,"= Infinity","\n")
  else:
   num_3 = num_1 ** (1/num_2)
   print(num_1,operator,num_2,"=",num_3,"\n")
 elif operator == "%":
  num_3 = (num_1/100) * num_2
  print(num_1,operator,"of",num_2,"=",num_3,"\n")
 elif operator=="mod":
  if num_2 == 0:
   print(num_1,operator,num_2,"= Infinity","\n")
  else:
   num_3 = num_1 % num_2
   print(num_1,operator,num_2,"=",num_3,"\n")	
 else:
  print("Invalid operation!","\n")
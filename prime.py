while True:
 n=int(input("Enter a number:"))
 if n<2:
  result="neither prime nor composite"
 else:
  for i in range(2,n):
   if n % i == 0:
    result="a composite"
    break
   else:
    result="a prime"
 print(f"{n} is {result} number.")
 print()

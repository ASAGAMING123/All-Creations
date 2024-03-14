import time
while True:
 n = int(input("Enter a number:"))
 while n>0:
  print(n)
  n-=1
  time.sleep(1)
 print("Happy New Year!")
import math 
while True:
    n = int(input("Enter ⊖ (angle in degrees):"))
    print()
    print(f"sin {n}{chr(176)} = {math.sin(math.radians(n))}")
    print(f"cos {n}{chr(176)} = {math.cos(math.radians(n))}")
    print(f"tan {n}{chr(176)} = {math.tan(math.radians(n))}")
    if math.sin(math.radians(n))==0:
     print(f"cosec {n}{chr(176)} = Infinity")
    else:
     print(f"cosec {n}{chr(176)} = {1/math.sin(math.radians(n))}")
    if math.cos(math.radians(n))==0:
     print(f"sec {n}{chr(176)} = Infinity")
    else:
     print(f"sec {n}{chr(176)} = {1/math.cos(math.radians(n))}")
    if math.tan(math.radians(n))==0:
     print(f"cot {n}{chr(176)} = Infinity")
    else:
     print(f"cot {n}{chr(176)} = {1/math.tan(math.radians(n))}")
    print()
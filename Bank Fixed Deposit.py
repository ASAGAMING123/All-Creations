Principal = float(input("Enter the Depositing Amount (in '₹'):"))
Time = float(input("Enter the time (in 'years'):"))
if Principal < 6000 and Time >= 2:
    Amount = Principal*(1+6/100)**Time
    print(f"The total amount is '{Amount}'.")
elif Principal > 6000 and Time >= 1:
    Amount = Principal*(1+8/100)**Time
    print(f"The total amount is '{Amount}'.")
elif Time >= 5:
    Amount = Principal*(1+10/100)**Time
    print(f"The total amount is '{Amount}'.")
else:
    Amount = Principal*(1+3/100)**Time
    print(f"The total amount is '{Amount}'.")

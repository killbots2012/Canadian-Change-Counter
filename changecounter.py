import sys
import math


# nicklesInput = int(input("how many nickles do you have? "))
# nicklesTotal = (nicklesInput * 0.05)
# print (f"{nicklesTotal}")
# # Dimes
# dimesInput = int(input("how many dimes do you have? "))
# dimesTotal = (dimesInput * 0.10)
# print (f"{dimesTotal}")
# Total = print (dimesTotal + nicklesTotal) 

# Nickels
try:
    nickelsInput = int(input("How many nickels do you have? "))
except ValueError:
    print("Please use numbers")
    continue
else:
    nickelsTotal = nickelsInput * 0.05
    print(f"Total value of nickels: ${nickelsTotal:.2f}")
    break

# Dimes
try:
    dimesInput = int(input("How many dimes do you have? "))
except ValueError:
        print("Please use numbers.")
else:
        dimesTotal = dimesInput * 0.10
        print(f"Total value of dimes: ${dimesTotal:.2f}")

# Quarters
try:
    quartersInput = int(input("How many Quarters do you have? "))
except ValueError:
    print("Please use numbers")
else:    
    quarterTotal = quartersInput * 0.25
    print(f"Total value of Quarters: ${quarterTotal:.2f}")

# Loonies
try:
    loonieInput = int(input("How Many Loonies do you have? "))
except ValueError:
    prink("Please use numbers instead")
else:
    loonieTotal = loonieInput * 1.00
    print(f"Total value of Loonies: ${loonieTotal:.2f}")

# Toonies
try:
    tooniesInput = int(input("How many Toonies do you have? "))
except ValueError:
    print("Please use numbers")
    tooniesInput = int(input("How many Toonies do you have? "))
else:    
    tooniesTotal = tooniesInput * 2.00
    print(f"Total Value of Toonies: ${tooniesTotal:.2f}")

# # Total
# total = dimesTotal + nickelsTotal + quarterTotal + loonieTotal + tooniesTotal
# print(f"Total value of change is: ${total:.2f}")
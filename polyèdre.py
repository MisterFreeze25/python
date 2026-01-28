import math

poly = input()
a = float(input())

if poly == 'T':
    print((math.sqrt(2) / 12) * a**3)
elif poly == 'C':
    print(a**3)
elif poly == 'O':
    print((math.sqrt(2) / 3) * a**3)
elif poly == 'D':
    print((a**3 / 4) * (15 + 7 * math.sqrt(5)))
elif poly == 'I':
    print((5 * (3 + math.sqrt(5)) / 12) * a**3)
else:
    print("Polyèdre non connu")
import pandas as pd

l1 = [2, 4]
l2 = [1, 3]

s1 = pd.Series(l1)
s2 = pd.Series(l2)

addition = s1 + s2

subtraction = s1 - s2

multiplication = s1 * s2

division = s1 / s2

print("Addition:")
print(addition)

print("Subtraction:")
print(subtraction)

print("Multiplication:")
print(multiplication)

print("Division:")
print(division)


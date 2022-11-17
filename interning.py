# num1 = -5    # implicit的整數interning範圍為-5 ~ 256。
# num2 = -5
# print(f'{num1 = }\t\t{num2 = }')
# print(f'{id(num1) = :<20}{id(num2) = }')
# print(f'{(id(num1) == id(num2)) = }')

# print()
# num1 = -6**99
# num2 = -6**99
# print(f'{num1 = }\t\t{num2 = }')
# print(f'{id(num1) = :<20}{id(num2) = }')
# print(f'{(id(num1) == id(num2)) = }')

# print()
# num1 = 256
# num2 = 256
# print(f'{num1 = }\t\t{num2 = }')
# print(f'{id(num1) = :<20}{id(num2) = }')
# print(f'{(id(num1) == id(num2)) = }')

print()
num = 999999999999999999999999*9999999999999999999999999999999999*999999999999999999999999
num1 = 999999999999999999999999*9999999999999999999999999999999999*999999999999999999999999
num2 = 999999999999999999999999*9999999999999999999999999999999999*999999999999999999999999
print(f'{num1 = }\t\t{num2 = }')
print(f'{id(num1) = :<20}{id(num2) = }')
print(f'{(id(num1) == id(num2)) = }')
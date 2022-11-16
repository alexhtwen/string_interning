import sys

head = 'A'
tail = 'lex'
str1 = sys.intern(head + tail)
str2 = sys.intern(head + tail)

print(str1, str2)
print(id(str1), id(str2))
# print(f'{str1 = }\t\t\t{str2 = }')
print(f'{id(str1) = :<20}{id(str2) = }')
print(f'{(id(str1) == id(str2)) = }')
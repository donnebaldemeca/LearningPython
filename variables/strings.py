name = 'donne'

# length of a string
print(len(name))

# finds the first index of character in a string
print(name.find('n'))

# string methods
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())

# checks to see if string only contains alphabetical characters
print(name.isalpha())

# replaces all old characters with new characters
print(name.replace('n', 'm'))

# prints string multiple times
print(name * 3)

# using F-strings
age = 31
print(f'hello {name}, i will call you {name * 2}\n'
      f'{name * 2}, you are {31} years old')

# .2f format is a floating point displaying 2 decimal places
x = 10.0
y = 3.0

# works even if x & y are both integers
print(f'10/3 = {x / y: .2f}')
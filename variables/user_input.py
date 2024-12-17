# input object that prints string parameter, and stores user input as a STRING type value
name = input('What is your name?\n')

# cast user inputted string value into integer datatype
age = int(input('What is your age?\n'))

age += 5

print(f'Hello {name}')
print(f'You will be {age} years-old in 5 years')
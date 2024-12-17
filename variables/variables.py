# Simple calculations
age = 21
age += 1

print(age)
print(type(age))

# Type error, cannot concatenate int to a str
# age ='21'
# age += 1
# print(age)
#
# Type error, cannot concatenate int to a str
# print("Age: " + age)

# Type cast
print ("Age: " + str(age)) # See ln 13

# Float datatype
height = 5.75

print("Height: "+str(height)+" ft")

# Boolean datatype
human = True
print(human)

# Type error, cannot concatenate bool to str
# print("Human: " + human)

# Type cast
print("Human: " + str(human)) # See ln 28

# Multiple variable assignments
name, age, working = "Donne", 31, True
print(name)
print(age)
print(working)

print(name, age, working)

print(name, age, working, sep='\n') # Change separation from a space to new line

# Variables that share the same value
age_person_1 = 25
age_person_2 = 25
age_person_3 = 25
age_person_4 = 25

print(age_person_1, age_person_2, age_person_3, age_person_4)

age_person_1 = age_person_2 = age_person_3 = age_person_4 = 30

print(age_person_1, age_person_2, age_person_3, age_person_4)

age_person_1 = 12

print(age_person_1, age_person_2, age_person_3, age_person_4)

age_person_2 = age_person_1

print(age_person_1, age_person_2, age_person_3, age_person_4)

age_person_1 = 18

print(age_person_1, age_person_2, age_person_3, age_person_4)

# Multiple Assignment

age_person_1 = age_person_2 = age_person_3 = age_person_4 = 30

print(age_person_1, age_person_2, age_person_3, age_person_4)

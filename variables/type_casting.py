x = 1 # int
y = 2.0 # float
z = '3' # str

# type casting int
y = int(y)
z = int(z)

print(y*z)
print(z*3)

# type casting float
x = float(x)
z = float(z)

print(x*z)
print(z*3)

# can be used when function does not accept certain datatypes
print ('x = ' + str(z)) # print will not take z as a floating point number

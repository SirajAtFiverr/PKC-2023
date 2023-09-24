
# Type Conversion
# int() float() str() 

a = 12
b = 12.4
x = "23"
y = "34.4"
c = " string"

# implicit type conversion (automatically)
d = a * b
print(type(d)) # float

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
e = d + c 

# explicit type conversion (manually)
f = str(a) + c
g = a + int(x)
h = float(y) + b

print(f, g, h)
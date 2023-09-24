
# Relational Operators/Comparision Operators/Conditional Operators
# These operators are used to compare two values and return a boolean value (True or False)
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

print(5 > 3) # True
print(5 < 3) # False
print(4 == 2) # False
print(4 != 2) # True
print(4 >= 4) # True
print(4 <= 3) # False
print(True == False) # False
print(True != False) # True

# Logical Operators
# These operators are used to combine two or more conditions
# and - returns True if both conditions are True
# or - returns True if any one of the conditions is True
# not - returns True if the condition is False and vice versa

print(5 > 3 and 4 < 2) # False
print(5 > 3 or 4 < 2) # True
print(not(5 > 3 and 4 < 2)) # True
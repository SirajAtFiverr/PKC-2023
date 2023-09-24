
# loops are used to iterate over a sequence of elements
# Types of loops: for loop, while loop

# for loop
for i in range(5):
    print(i)

# range() function
# range(start, stop, step)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1

# program to print all the even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
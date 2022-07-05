# Notes from Corey Schafer's Python Course
# https://www.youtube.com/c/Coreyms

nums = [1,2,3,4,5]

for num in nums:
    print(num)
 
# Output
# 1
# 2
# 3
# 4
# 5

# Break Statment

nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print ("Found 3")
        break
    print(num)

# Output
# 1
# 2
# Found 3

nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num)

# Output
# 1
# 2
# Found
# 4
# 5

nums = [1,2,3,4,5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

# output
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# ...
# 5 c

# Range function
for i in range(10):
    print(i)

 # output
 # prints 0 - 10

# Start at 1
for i in range (1, 11):
     print(i)
# output
# prints 1 - 10

# while loops, goes until condition or break is met
x = 0

while x < 10:
    print(x)
    x += 1
# Output
# prints 0 - 10

# break at 5

y = 0
while y < 10:
    if y == 5:
        break
    print(y)
    y+= 1
# Output
# prints 0 - 4

# inf loop use value of true
while True:
    if x == 5:
        break
    print(x)
    x+=1

 # Output
 # Prints  0 -4 and breaks out at 5 (same as above)

x = 0

#while True:
#     print(x)
#     x +=1

# Output
# This will count forever break with ctl+c


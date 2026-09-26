count = 1
total = 0

# BUG: Added the missing colon after the while condition.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted total to a string because Python cannot concatenate a string and an integer with +.
print("Sum of 1 to 5 is: " + str(total))

# BUG: Changed < 5 to <= 5 so that 5 is included in the calculation.
#Python Code Challenges involving Control Flow
#Large Power
#For the first code challenge, we are going to create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:

# Create a function named large_power() that takes two parameters named base and exponent.

#If base raised to the exponent is greater than 5000, return True, otherwise return False

#Hint: Make sure you use if and else statements to return True or return False. Also, to take the power of one number to another number you can use the ** operator.

# Write your large_power function here:

def large_power(base, exponent):
	if base ** exponent > 5000:
		return True
	else:
		return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
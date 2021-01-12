# Testing if a number falls within a certain range
# Define the function to accept three numbers as parameters
# Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound
# If this is true, return True, otherwise, return False

# Write your in_range function here:
def in_range(num,lower,upper):
    if num >= lower and num <= upper:
      return True
    else:
      return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

# another way to implement this would be 
def in_range_two(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False
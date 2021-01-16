def initials():
  print("BBBB" + "  " + " BBBB") 
  print("B" + "   " + "B" + "  " + "B" + "   " + "B" )
  print("B" + "   " + "B" + "  " + "B" + "   " + "B" )
  print("BBBB" + "  " + " BBBB")
  print("B" + "   " + "B" + "  " + "B" + "   " + "B" )
  print("B" + "   " + "B" + "  " + "B" + "   " + "B" )
  print("BBBB" + "  " + " BBBB")

#call the function which should print "BB" to the screen in block letters!

# BBBB   BBBB
# B   B  B   B
# B   B  B   B
# BBBB   BBBB
# B   B  B   B
# B   B  B   B
# BBBB   BBBB
#function call below
# initials()

def divide_two_numbers(x, y):
  result = x / y
  return result
 
# try:
#   result = divide_two_numbers(2,0)
#   print(result)
# except NameError:
#   print("A NameError occurred.")
# except ValueError:
#   print("A ValueError occurred.") 
# except ZeroDivisionError:
#   print("A ZeroDivisionError occurred.")
 

 # Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
	if budget < (food_bill + electricity_bill + internet_bill +rent):
		return True
	else:
		return False


# Uncomment these function calls to test your over_budget function:
# print(over_budget(100, 20, 30, 10, 40))
# should print False
# print(over_budget(80, 20, 30, 10, 30))
# should print True

# Create a function named twice_as_large() that has two parameters named num1 and num2.

# Return True if num1 is more than double num2. Return False otherwise.

def twice_as_large(num1, num2):
	if num1 > (2 * num2):
		return True
	else:
		return False

#your twice_as_large function:
#print(twice_as_large(10, 5))
# should print False
#print(twice_as_large(11, 5))
# should print True

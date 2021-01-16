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
# initials()

# def divide_two_numbers(x, y):
#   result = x / y
#   return result
 
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
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

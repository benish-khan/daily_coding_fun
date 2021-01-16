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
initials()

def divide_two_numbers(x, y):
  result = x / y
  return result
 
try:
  result = divide_two_numbers(2,0)
  print(result)
except NameError:
  print("A NameError occurred.")
except ValueError:
  print("A ValueError occurred.") 
except ZeroDivisionError:
  print("A ZeroDivisionError occurred.")
 

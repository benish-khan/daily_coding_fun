# This function will accept both of those values as inputs and return the amount of money to tip.
# Define the function to accept the total cost of the food called total and the percentage to tip as percentage
# Calculate the tip amount by multiplying the total and percentage and dividing by 100
# Return the tip amount

def tip(total, percentage):
    tip_amount = (total * percentage) / 100

    return tip_amount 

# should print 2.5
print(tip(10, 25))
# should print 0.0
print(tip(0, 100))
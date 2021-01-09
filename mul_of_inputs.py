# Define the function header to accept one input parameter called num
# Print out 1 times num
# Print out 2 times num
# Print out 3 times num
# Return the value of 3 times num
def first_three_multiples(num): 
    a = num * 1
    print(a)
    b = num * 2
    print(b) 
    c = num * 3
    print(c)
    return(c)

# Uncomment these function calls to test your first_three_multiples function:   
first_three_multiples(2)
# should print 2, 4, 6, and return 6
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
# Create a function named double_index that has two parameters: 
# a list named lst 
# and a single number named index.

# The function should return a new list where all elements are the same as in lst 
# except for the element at index.
#  The element at index should be double the value of the element at index 
#  of the original lst.

# If index is not a valid index, the function should return the original list.

# For example, the following code should return [1,2,6,4] 
# because the element at index 2 has been doubled:

# test function works with this input double_index([1, 2, 3, 4], 2)

# We can use slicing to get the values up to an index lst[0:index]
# and from an index to the end lst[index+1:]. 
# Also, to append to the end of a list we can use the append() function.

def double_index(lst, index):
	first_3 = lst[0:index]
	the_rest_of_lst = lst[index+1:]
	new_lst = []

	for i in first_3:
		new_lst.append(i)
		if lst[index]:
			new_lst.append(lst[index] * 2)
	for i in the_rest_of_lst:
		new_lst.append(i)

	return new_lst

test_this = double_index([1, 2, 3, 4], 2)

print(test_this) # [1, 6, 2, 6, 4]

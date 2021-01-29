ef divisible_by_ten(nums):
  count = 0
  for n in nums:
    if n % 10 == 0:
      count += 1
  return count


#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
#expected: 3 because 20,30and 40 are all divisible by 10. 


def add_greetings(names):
  empty_lst = []
  for name in names:
    empty_lst.append("Hello, " + name)
  return empty_lst

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
#expected: ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
      lst = lst[1:]
  return lst


#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst)):
    if index % 2 != 0:
      new_lst.append(lst[index])
  return new_lst
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

"""
The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list. 
For example, odd_indices([4, 3, 7, 10, 11, -2])
should return the list [3, 10, -2]

"""

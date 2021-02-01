#Write your function here
def larger_sum(lst1, lst2):
  if sum(lst1) > sum(lst2):
    return lst1
  elif sum(lst1) < sum(lst2):
    return lst2
  else:
    return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7])) #expect to print lst1
print(larger_sum([2, 4, 9], [1, 9, 5],)) #expect to print lst2
print(larger_sum([2, 3, 7], [2, 3, 7],)) #expect to print lst1

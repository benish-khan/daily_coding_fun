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



print(over_nine_thousand([8000, 900, 120, 5000]))
def over_nine_thousand(lst):
  count = 0
  for i in lst:
    count += i
    if count > 9000:
      break
    elif count < 9000:
      return sum(lst)
    elif len(lst) < 1:
      return 0
  return count



#print(over_nine_thousand([8000, 900, 120, 5000])) #expecting 9020
#print(over_nine_thousand([])) #expecting 0
#print(over_nine_thousand([8000, 120])) expecting 8120

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum 

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

def username_generator(first_name, last_name):
  user_name = ""
  if len(first_name) < 3:
    user_name = first_name
  else:
    user_name = first_name[0:3]
  if len(last_name) < 4:
    user_name = user_name + last_name
  else:
    user_name = user_name + last_name[0:4]
  return user_name 
test_1 = username_generator("abe", "simpson")
print(test_1) 

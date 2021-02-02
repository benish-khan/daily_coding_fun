first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[0:3] + last_name[0:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)

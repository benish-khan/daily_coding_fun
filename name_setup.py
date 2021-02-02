first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[0:3] + last_name[0:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)

txt = "She said \"never let go\"."  # should print She said "never let go".
print(txt)


name ="saudah"

print("b" in name) #return False
print("u" in name) #return True

a = "me"
b = " she"
c = a + b
print(c) # print me she

str = "car"
for c in str:
    print(c + c.upper() + c + c.upper())

    """
    cCcC
    aAaA
    rRrR
    """

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  for name in first_name:
    length_first = len(first_name)
    last_3_char_first = first_name[length_first-3:]
  for name in last_name:
    length_last = len(last_name)
    last_3_char_last = last_name[length_last-3:]
  return last_3_char_first + last_3_char_last

new_pswd = print(password_generator(first_name, last_name))

make_upper = 'make upper'.upper()
print(make_upper)

make_lower = 'maKA LOWER'.lower()
print(make_lower)

make_title = 'make title'.title()
print(make_title)

make_split = 'make title split'.split()
print(make_split)

make_join = ' '.join("Hello", "world!")
print(make_join)

make_replace = 'hello world'.replace('h', 'j')
print(make_replace)

https://gist.github.com/00a90a5ef34c649cc291c21eeed1b4e2

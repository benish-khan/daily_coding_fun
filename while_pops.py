
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
print(students_in_poetry)

#expected result of this is "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"

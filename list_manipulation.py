names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

age = []

age.append(42)

all_ages = [32, 41, 29] + age

name_and_age = zip(first_names, age)

ids = range(4)

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]

subjects.append("computer science")

grades = [98, 97, 85, 88]
grades.append(100)
gradebook = list(zip(grades, subjects))
gradebook.append(("93", "visual arts"))
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
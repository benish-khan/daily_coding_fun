statement_one = False

statement_two = True  
def graduation_reqs(gpa, credits):
  if gpa >= 2.0 and credits >= 120:
    return "You meet the requirements to graduate!"

  elif gpa >= 2.0 and credits != 120:
    return "You do not have enough credits to graduate."

  elif gpa < 2.0 and credits >= 120:
    return "Your GPA is not high enough to graduate."

  elif credits < 120 and gpa < 2.0:
    return "You do not meet either requirement to graduate!"

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



def grade_converter(gpa):
  grade = None
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  elif gpa >= 0.0:
    return "F"
    
print(grade_converter(3.0))
# should return B
print(grade_converter(2.0))
# should return C
print(grade_converter(1.0))
# should return D
print(grade_converter(0.0))
# should return F
print(grade_converter(4.0))
# should return A
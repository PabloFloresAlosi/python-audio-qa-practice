# Exercise 10 — Localization Discount Logic

# Concepts practiced:

# if
# else
# nested if
# comparison operators
# booleans

# Goal: convertir este gráfico de decisión a código.

# age = 16
# is_student = True

#                     age
#                      |
#               Is age < 18?
#               /          \
#            True          False
#             |              |
#       Is student?      Regular price
#        /      \
#     True      False
#      |          |
# 20% discount  10% discount

# Instructions:

# Create these variables:

# age = 16
# is_student = True

# Rules:

# If age is lower than 18, check if the person is a student.

# If the person is under 18 and is a student, print:

# 20% discount

# If the person is under 18 but is not a student, print:

# 10% discount

# If the person is 18 or older, print:

# Regular price

# Expected output:

# 20% discount

# Important: this one should use a nested if.

# Structure hint:

# if age < 18:
#     if is_student == True:
#         print(...)
#     else:
#         print(...)
# else:
#     print(...)
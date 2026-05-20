# Exercise 06 — Footstep Surface QA Checker

# Concepts practiced:

# input()
# float()
# int()
# comparisons
# booleans
# f-strings
# print()

# # Exercise 06 — Footstep Surface QA Checker

# # Ask the user for:
# # Enter surface name:
# # Enter footstep duration:
# # Enter number of variations:

surface_type = input("Surface Type: ")
footstep_duration = input("Footstep duration: ")
variation_number = input("Variation number: ")

# # Example input:
# # Wood
# # 0.45
# # 6

# # Convert footstep_duration to float.
# # Convert number_of_variations to int.

footstep_duration = float(footstep_duration)
variation_number = int(variation_number)

# # Create these checks:
# # duration_is_ok = footstep_duration >= 0.2
# # variations_are_ok = number_of_variations >= 4

duration_is_ok = footstep_duration >= 0.2
variations_are_ok = variation_number >= 4

# # Then print:
# # Surface checked: Wood
# # Duration OK: True
# # Enough variations: True

print(f"Surface checked: {surface_type}")
print(f"Duration OK: {duration_is_ok}")
print(f"Enough variations: {variations_are_ok}")

# Expected output with the example input:

# Surface checked: Wood
# Duration OK: True
# Enough variations: True

# Pista:

# footstep_duration = float(footstep_duration)
# number_of_variations = int(number_of_variations)
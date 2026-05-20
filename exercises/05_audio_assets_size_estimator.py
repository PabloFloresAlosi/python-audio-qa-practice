# Exercise 05 — Audio Asset Size Estimator

# Concepts practiced:

# Numbers
# Basic math
# Variables
# f-strings
# print()
# Type conversion with str() or f-strings

# # Exercise 05 — Audio Asset Size Estimator

# # Create these variables:
# # file_name = "AMB_Forest_Loop_01.wav"
# # duration_seconds = 30
# # size_per_second_mb = 0.5

file_name = "AMB_Forest_Loop_01.wav"
duration_seconds = 30
size_per_second_mb = 0.5

# # Calculate the estimated file size:
# # estimated_size_mb = duration_seconds * size_per_second_mb

estimated_size_mb = duration_seconds * size_per_second_mb

# # Then print:
# # File: AMB_Forest_Loop_01.wav
# # Duration: 30 seconds
# # Estimated size: 15.0 MB

print(f"File: {file_name}")
print(f"Duration: {duration_seconds} seconds")
print(f"Estimated Size: {estimated_size_mb} MB")

# Expected output:

# File: AMB_Forest_Loop_01.wav
# Duration: 30 seconds
# Estimated size: 15.0 MB

# Pista:

# estimated_size_mb = duration_seconds * size_per_second_mb
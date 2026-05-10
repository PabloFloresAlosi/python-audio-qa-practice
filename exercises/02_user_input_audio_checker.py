# Exercise 02 — User Input Audio Checker

# Create a program that asks the user for these values using input():

# Enter file name:
# Enter duration:
# Enter sample rate:

# Example values you could enter:

# VO_ES_MA_Complaint_R_004_A.wav
# 0.25
# 44100

# After that, the program should print:

# File checked: VO_ES_MA_Complaint_R_004_A.wav
# Duration is valid: False
# Sample rate is valid: False

# Rules:

# The duration must be converted to float.

# The sample rate must be converted to int.

# The duration is valid if it is greater than 0.3.

# The sample rate is valid if it is equal to 48000.

# Do not use if yet. Only print True or False.

# Hint:

# duration = float(duration)
# sample_rate = int(sample_rate)

# Exercise 02 — User Input Audio Checker

file_name = input("Enter file name: ")
duration = input("Enter duration: ")
sample_rate = input("Enter sample rate: ")

duration = float(duration)
sample_rate = int(sample_rate)

duration_is_valid = duration > 0.3
sample_rate_is_valid = sample_rate == 48000

print(f"File checked: {file_name}")
print(f"Duration is valid: {duration_is_valid}")
print(f"Sample rate is valid: {sample_rate_is_valid}")

# Exercise 01 — Audio File Info Printer

# Create a program that stores this information in variables:

# language = "EN"
# character = "FA"
# category = "Work"
# line_type = "Q"
# id_number = "003"
# variation = "A"
# duration = 1.42
# sample_rate = 48000

# The program should print something like this:

# File: VO_EN_FA_Work_Q_003_A.wav
# Duration: 1.42 seconds
# Sample rate: 48000 Hz

# Rules:

# Do not write the full file name directly. You must build it using the variables.

# Hint:

# file_name = "VO_" + language + "_" + character

# But complete the full file name.

# Exercise 01 — Audio File Info Printer

languague = "EN"
character = "FA"
category = "Work"
line_type = "Q"
id_number = "003"
variation = "A"
duration = 1.42
sample_rate = 48000 

file_name = "VO_" + languague + "_" + character + "_" + category + "_" + line_type + "_" + id_number + "_" + variation + ".wav"
file_alternative = f"VO_{languague}_{character}_{category}_{line_type}_{id_number}_{variation}.wav"

print("File: " + file_name)
print("Duration: " + str(duration) + " seconds")
print("Sample rate: " + str(sample_rate) + " Hz")
print(f"File Alternative: {file_alternative}")
print(f"Duration Alternative: {duration} seconds")
print(f"Sample rate Alternative: {sample_rate} Hz")

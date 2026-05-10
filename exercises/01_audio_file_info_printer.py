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

language = "EN"
character = "FA"
category = "Work"
line_type = "Q"
id_number = "003"
variation = "A"
duration = 1.42
sample_rate = 48000

file_name = f"VO_{language}_{character}_{category}_{line_type}_{id_number}_{variation}.wav"

print(f"File: {file_name}")
print(f"Duration: {duration} seconds")
print(f"Sample rate: {sample_rate} Hz")

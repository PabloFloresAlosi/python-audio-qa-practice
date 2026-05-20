# Exercise 07 — For Loop Audio List Checker

# Concepts practiced:

# Lists
# for loops
# in
# Basic string checking
# Control flow with if

# # Exercise 07 — For Loop Audio List Checker

# # Create this list:
# # files = [
# #     "VO_EN_FA_Work_Q_003_A.wav",
# #     "VO_ES_MA_Complaint_R_004_A.wav",
# #     "VO_ES_FA_Greeting_Q_001_A.wav",
# #     "VO_EN_MA_Idle_R_002_A.wav"
# # ]

files = [
     "VO_EN_FA_Work_Q_003_A.wav",
     "VO_ES_MA_Complaint_R_004_A.wav",
     "VO_ES_FA_Greeting_Q_001_A.wav",
     "VO_EN_MA_Idle_R_002_A.wav"
]

# # Use a for loop to check each file.
# # If the file contains "_ES_", print:
# # Spanish file: [file name]

# # Otherwise, print:
# # Not Spanish: [file name]

for file_name in files:
    if "_ES_" in file_name:
        print(f"Spanish file: {file_name}")
    else:
        print(f"Not Spanish: {file_name}")

# Expected output:
# Not Spanish: VO_EN_FA_Work_Q_003_A.wav
# Spanish file: VO_ES_MA_Complaint_R_004_A.wav
# Spanish file: VO_ES_FA_Greeting_Q_001_A.wav
# Not Spanish: VO_EN_MA_Idle_R_002_A.wav

# Pista:
# for file_name in files:
#     if "_ES_" in file_name:
#         print(f"Spanish file: {file_name}")
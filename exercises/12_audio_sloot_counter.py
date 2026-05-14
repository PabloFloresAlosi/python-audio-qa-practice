# Exercise 12 — While Loop Ticket / Audio Slot Counter

# Concepts practiced:

# while loop
# conditionals inside loops
# counter update
# if
# else

# Goal: usar un loop que va bajando un contador y reacciona cuando quedan pocos slots.

# audio_slots = 5

#               audio_slots > 0?
#               /              \
#            True              False
#             |                  |
#      Print current slot      End loop
#             |
#      Is audio_slots == 1?
#         /          \
#      True          False
#       |              |
# Print "Last slot"  Print "Processing slot"
#             |
#     audio_slots = audio_slots - 1
#             |
#        Repeat loop

# Instructions:

# Create this variable:

# audio_slots = 5

# Use a while loop that runs while audio_slots > 0.

# Inside the loop:

# Print:

# Slots remaining: 5

# Then:

# If audio_slots is equal to 1, print:

# Last slot

# Otherwise, print:

# Processing slot

# At the end of each loop, subtract 1 from audio_slots.

# Expected output:

# Slots remaining: 5
# Processing slot
# Slots remaining: 4
# Processing slot
# Slots remaining: 3
# Processing slot
# Slots remaining: 2
# Processing slot
# Slots remaining: 1
# Last slot

# Important hint:

# audio_slots = audio_slots - 1

# must be inside the loop. If you forget that line, the loop never ends
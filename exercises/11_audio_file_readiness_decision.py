# Exercise 11 — Audio File Readiness Decision

# Concepts practiced:

# if
# elif
# else
# and
# comparison operators
# boolean logic

# Goal: revisar si un archivo de audio está listo, necesita conversión o debe ir a revisión.

# sample_rate = 44100
# duration = 1.5
# has_spaces = False

#                          file data
#                             |
#                     Is duration <= 0.3?
#                      /              \
#                   True              False
#                    |                  |
#           Print "Review: too short"  Is sample_rate != 48000?
#                                       /              \
#                                    True              False
#                                     |                  |
#                    Print "Convert sample rate"   Does name have spaces?
#                                                     /          \
#                                                  True          False
#                                                   |              |
#                                Print "Fix file name"     Print "Ready"

# Instructions:

# Create these variables:

# sample_rate = 44100
# duration = 1.5
# has_spaces = False

# Rules:

# If duration is less than or equal to 0.3, print:

# Review: too short

# Else if sample_rate is not equal to 48000, print:

# Convert sample rate

# Else if has_spaces is True, print:

# Fix file name

# Otherwise, print:

# Ready

# Expected output:

# Convert sample rate

# Try changing the values:

# duration = 0.2
# sample_rate = 48000
# has_spaces = False

# Expected:

# Review: too short

# Then try:

# duration = 1.2
# sample_rate = 48000
# has_spaces = True

# Expected:

# Fix file name
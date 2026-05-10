# Exercise 03 — Mini Localization QA Validator

# Create these variables:

# file_name = "VO_ES_FA_Greeting_Q_001_A.wav"
# expected_language = "ES"
# duration = 1.8
# sample_rate = 48000
# has_spaces = False

# Now create these checks:

# language_is_correct = expected_language in file_name
# duration_is_ok = duration > 0.3
# sample_rate_is_ok = sample_rate == 48000
# naming_is_ok = has_spaces == False
# file_is_ready = language_is_correct and duration_is_ok and sample_rate_is_ok and naming_is_ok

# Then print:

# Language OK: True
# Duration OK: True
# Sample rate OK: True
# Naming OK: True
# File ready for pipeline: True

# Then change some values to break the validation, for example:

# sample_rate = 44100

# And check that file_is_ready becomes False.

# Exercise 03 — Mini Localization QA Validator

file_name = "VO_ES_FA_Greeting_Q_001_A.wav"
expected_language = "ES"
duration = 1.8
sample_rate = 48000
has_spaces = False

language_is_correct = expected_language in file_name
duration_is_ok = duration > 0.3
sample_rate_is_ok = sample_rate == 48000
naming_is_ok = has_spaces == False

file_is_ready = (
    language_is_correct
    and duration_is_ok
    and sample_rate_is_ok
    and naming_is_ok
)

print(f"Language OK: {language_is_correct}")
print(f"Duration OK: {duration_is_ok}")
print(f"Sample rate OK: {sample_rate_is_ok}")
print(f"Naming OK: {naming_is_ok}")
print(f"File ready for pipeline: {file_is_ready}")

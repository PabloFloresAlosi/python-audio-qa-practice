# Exercise 08 — Full Mini Audio QA Pipeline

# Este es el ejercicio con todo incluido. Aquí mezclamos:

# Variables
# Strings
# Lists
# For loops
# If / else
# Booleans
# Comparisons
# and
# f-strings
# Control flow
# Mentalidad QA real

# Goal: revisar una lista de archivos de audio y decidir si cada archivo pasa o necesita revisión.

# Copia esta data inicial:

# # Exercise 08 — Full Mini Audio QA Pipeline

# files = [
#     "VO_EN_FA_Work_Q_003_A.wav",
#     "VO_ES_MA_Complaint_R_004_A.wav",
#     "VO_ES_FA_Greeting_Q_001_A.wav",
#     "VO EN MA Idle R 002 A.wav"
# ]

# durations = [
#     1.42,
#     0.25,
#     1.80,
#     2.10
# ]

# sample_rates = [
#     48000,
#     44100,
#     48000,
#     48000
# ]

# expected_language = "ES"

# Ahora el programa debe revisar cada archivo.

# Reglas:

# Un archivo está listo para el pipeline si:

# 1. Contains the expected language: "_ES_"
# 2. Duration is greater than 0.3
# 3. Sample rate is 48000
# 4. File name has no spaces

# Expected output:

# Checking: VO_EN_FA_Work_Q_003_A.wav
# Language OK: False
# Duration OK: True
# Sample rate OK: True
# Naming OK: True
# File ready: False
# ---

# Checking: VO_ES_MA_Complaint_R_004_A.wav
# Language OK: True
# Duration OK: False
# Sample rate OK: False
# Naming OK: True
# File ready: False
# ---

# Checking: VO_ES_FA_Greeting_Q_001_A.wav
# Language OK: True
# Duration OK: True
# Sample rate OK: True
# Naming OK: True
# File ready: True
# ---

# Checking: VO EN MA Idle R 002 A.wav
# Language OK: False
# Duration OK: True
# Sample rate OK: True
# Naming OK: False
# File ready: False
# ---

# Pistas importantes:

# Para recorrer listas por posición, puedes usar:

# for index in range(len(files)):

# Y luego acceder a cada dato así:

# file_name = files[index]
# duration = durations[index]
# sample_rate = sample_rates[index]

# Para revisar idioma:

# language_is_ok = f"_{expected_language}_" in file_name

# Para revisar espacios:

# naming_is_ok = " " not in file_name

# Para revisar si todo está listo:

# file_is_ready = language_is_ok and duration_is_ok and sample_rate_is_ok and naming_is_ok
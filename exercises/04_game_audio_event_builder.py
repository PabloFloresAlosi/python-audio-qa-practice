# Exercise 04 — Game Audio Event Label Builder

# Concepts practiced:

# Variables
# Strings
# f-strings
# print()

# # Exercise 04 — Game Audio Event Label Builder

# # Create these variables:
# # event_type = "UI"
# # action = "Confirm"
# # intensity = "Small"
# # variation = "02"

event_type = "UI"
action = "Confirm"
intensity = "Small"
variation = "02"

# # Build this event name using an f-string:
# # UI_Confirm_Small_02

event_name = f"{event_type}_{action}_{intensity}_{variation}"

# # Then print:
# # Audio event created: UI_Confirm_Small_02

print(f"Audio event created: {event_name}")

# Expected output:
# Audio event created: UI_Confirm_Small_02

# Pista:
# event_name = f"{event_type}_{action}"

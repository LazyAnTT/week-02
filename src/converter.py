# ===============================
# Conversion constants
# ===============================

KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

# ===============================
# Ask the user which conversion they want
# ===============================

print("Choose conversion:")
print("1) km <-> mi")
print("2) kg <-> lb")
print("3) L <-> gal")
print("4) USD <-> EUR")

conversion_type = input("> ")

# Variables that will be filled later
factor = 0
unit1 = ""
unit2 = ""

# Select conversion factor and unit names
if conversion_type == "1":
    factor = KM_TO_MI
    unit1 = "km"
    unit2 = "mi"
elif conversion_type == "2":
    factor = KG_TO_LB
    unit1 = "kg"
    unit2 = "lb"
elif conversion_type == "3":
    factor = L_TO_GAL
    unit1 = "L"
    unit2 = "gal"
elif conversion_type == "4":
    factor = USD_TO_EUR
    unit1 = "USD"
    unit2 = "EUR"
else:
    print("Invalid conversion choice.")
    exit()

# Ask for conversion direction
print(f"Direction: 1) {unit1} -> {unit2}  2) {unit2} -> {unit1}")
direction = input("> ")

# Keep asking until the user enters a valid number
while True:
    try:
        value = float(input("Enter value: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Perform conversion after a valid number is entered
if direction == "1":
    result = value * factor
    from_unit = unit1
    to_unit = unit2
elif direction == "2":
    result = value / factor
    from_unit = unit2
    to_unit = unit1
else:
    print("Invalid direction choice.")
    exit()

# Print result with 2 decimal places
print(f"{value:.2f} {from_unit} = {result:.2f} {to_unit}")
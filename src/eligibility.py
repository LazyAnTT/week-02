# ===============================
# Ask for age with error handling
# ===============================

try:
    age = int(input("Enter age: "))

    if age < 0:
        print("Age cannot be negative.")
        exit()

except ValueError:
    print("Invalid age input. Please enter a number.")
    exit()


# ===============================
# Ask yes/no questions
# ===============================

has_license = input("Do you have a driver's license? (y/n): ").lower() == "y"
is_student = input("Are you a student? (y/n): ").lower() == "y"
is_veteran = input("Are you a veteran? (y/n): ").lower() == "y"


# ===============================
# Eligibility logic
# ===============================

can_vote = age >= 18

can_rent_car = age >= 21 and has_license

senior_discount = age >= 65 or is_veteran

student_discount = (16 <= age <= 26) and is_student


# ===============================
# Print results
# ===============================

print("\n---")

print(f"Voting:           {'Yes ✓' if can_vote else 'No ✗'}")

if age >= 21 and not has_license:
    print(f"Car rental:       No ✗ (no license)")
else:
    print(f"Car rental:       {'Yes ✓' if can_rent_car else 'No ✗'}")

print(f"Senior discount:  {'Yes ✓' if senior_discount else 'No ✗'}")

print(f"Student discount: {'Yes ✓' if student_discount else 'No ✗'}")
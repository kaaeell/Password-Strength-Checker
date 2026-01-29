import string

print("Password Strength Checker\n")

password = input("Enter your password: ")

score = 0
feedback = []

# Check length
if len(password) >= 8:
    score += 1
    feedback.append("Contains at least 8 characters")
else:
    feedback.append("Less than 8 characters")

# Check lowercase letters
if any(char.islower() for char in password):
    score += 1
    feedback.append("Contains lowercase letters")
else:
    feedback.append("Missing lowercase letters")

# Check uppercase letters
if any(char.isupper() for char in password):
    score += 1
    feedback.append("Contains uppercase letters")
else:
    feedback.append("Missing uppercase letters")

# Check digits
if any(char.isdigit() for char in password):
    score += 1
    feedback.append("Contains numbers")
else:
    feedback.append("Missing numbers")

# Check special characters
if any(char in string.punctuation for char in password):
    score += 1
    feedback.append("Contains special characters")
else:
    feedback.append("Missing special characters")

# Determine strength
if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Strength:", strength)
print("Details:")
for item in feedback:
    print("-", item)

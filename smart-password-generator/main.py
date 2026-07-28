import secrets
import string

low = string.ascii_lowercase
up = string.ascii_uppercase
num = string.digits
spec = "!@#$%^&*()-+"

print("--- Smart Password Generator (Secure Version ---")

# Length input with validation
try:
    length = int(input("Enter the password length: "))
    if length <= 0:
        raise ValueError("Length must be positive")
except ValueError as e:
    print(f"Error: {e}")
    exit()

print("Include following character sets? (y/n)")
use_low = input("Lowercase (a-z)? ").lower() == "y"
use_up = input("Uppercase (A-Z)? ").lower() == "y"
use_num = input("Digits (0-9)? ").lower() == "y"
use_spec = input("Special symbols? ").lower() == "y"

# Pool construction
pool = ""
if use_low:
    pool += low
if use_up:
    pool += up
if use_num:
    pool += num
if use_spec:
    pool += spec

if not pool:
    print("Error: No character sets selected.")
    exit()

# Secure generation using secrets.choice
password = "".join(secrets.choice(pool) for _ in range(length))

print("\n" + "=" * 30)
print(f"Generated Password: {password}")
print("=" * 30)

# Security analysis
has_low = any(c in low for c in password)
has_up = any(c in up for c in password)
has_num = any(c in num for c in password)
has_spec = any(c in spec for c in password)
is_long = len(password) >= 8

score = sum([has_low, has_up, has_num, has_spec, is_long])

print("\n--- Security Report ---")
if score == 5:
    print("Strength: Strong ✅")
elif score >= 3:
    print("Strength: Medium ⚠️")
else:
    print("Strength: Weak ❌")

# Hints
if not is_long:
    print("- Hint: Increase length to 8+ symbols.")
if not has_low:
    print("- Hint: Add lowercase letters.")
if not has_up:
    print("- Hint: Add uppercase letters.")
if not has_num:
    print("- Hint: Add digits.")
if not has_spec:
    print("- Hint: Add special characters.")

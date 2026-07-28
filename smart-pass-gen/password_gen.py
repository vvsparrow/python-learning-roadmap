import random

# Basic character sets
low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
spec = "!@#$%^&*()-+"


print("--- Welcome to the Smart Password Generator ---")

# Length input with anti-fooling protection
try:
    length = int(input("Enter the password length: "))
except ValueError:
    print("Error: Please enter a number")
    exit()

print("Include following character sets? (y/n)")
use_low = input("Lowercase (a-z)? ").lower() == "y"
use_up = input("Uppercase (A-Z)? ").lower() == "y"
use_num = input("Digits (0-9)? ").lower() == "y"
use_spec = input("Special symbols? ").lower() == "y"

# Construct the pool based on choices
pool = ""
if use_low:
    pool += low
if use_up:
    pool += up
if use_num:
    pool += num
if use_spec:
    pool += spec

# Check if pool is empty
if not pool:
    print("Error: You must select at least one character set.")
    exit()

# Generate the password using a Generator Expression
password = "".join(random.choice(pool) for _ in range(length))


print("\n" + "-" * 30)
print(f"Generated Password: {password}")
print("-" * 30)

# Security checks using Generator Expressions and any()
has_low = any(char in low for char in password)
has_up = any(char in up for char in password)
has_num = any(char in num for char in password)
has_spec = any(char in spec for char in password)
is_long = len(password) >= 8

# Total score (sum of boolean values: True=1, False=0)
score = sum([has_low, has_up, has_num, has_spec, is_long])


print("\n--- Security Report ---")
if score == 5:
    print("Strength: STRONG ✅")
elif score >= 3:
    print("Strength: MEDIUM ⚠️")
else:
    print("Strength: WEAK ❌")

# Hints for improvement
if not is_long:
    print("- Hint: Increase length to at least 8 symbols.")
if not has_low:
    print("- Hint: Add lowercase letters.")
if not has_up:
    print("- Hint: Add uppercase letters.")
if not has_num:
    print("- Hint: Add digits.")
if not has_spec:
    print("- Hint: Add special characters.")

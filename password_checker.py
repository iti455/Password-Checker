import re

def check_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # FIX: Convert everything to boolean using bool()
    score = sum([
        bool(length),
        bool(upper),
        bool(lower),
        bool(digit),
        bool(special)
    ])

    print("\n🔎 Password Analysis:")
    print("✅ Length OK" if length else "❌ Minimum 8 characters")
    print("✅ Has Uppercase" if upper else "❌ Missing Uppercase")
    print("✅ Has Lowercase" if lower else "❌ Missing Lowercase")
    print("✅ Has Number" if digit else "❌ Missing Number")
    print("✅ Has Special Character" if special else "❌ Missing Special Character")

    print(f"\n🔐 Strength Score: {score}/5")
    if score == 5:
        print("💪 Password is Strong")
    elif score >= 3:
        print("🟡 Password is Moderate")
    else:
        print("🔴 Password is Weak")

# Input from user
password = input("🔑 Enter your password: ")
check_strength(password)

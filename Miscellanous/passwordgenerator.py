import secrets
import string
print("PASSWORD GENERATOR")
safe_punct = "!@#$%^&*()-_=+[]{}|;:,.<>?"
while True:
    length = int(input("Enter password length: "))
    if length < 8:
        print("Passwords under 8 characters long are highly vulnerable and can be hacked instantly to a few minutes")
        continue
    chars = string.ascii_letters + string.digits + safe_punct
    password = "".join(secrets.choice(chars) for _ in range(length))
    
    print(f"Secure password: {password}\n")
secret = "fez"
response = input("Enter the secret word: ").lower().strip()

if response == secret   :
    print("Yes! That's the secret word.")
else:
    print("Nope. That's not the secret word.")

pin = "1111"

attempt = 0
passed = 0

while attempt < 3:
    guess = input("Enter PIN: ")
    if guess != pin:
        attempt += 1
        print(f"Incorrect, {3 - attempt} attempts left")
    else:
        print("Payment accepted")
        passed = 1

if passed != 1:
    print("card blocked")
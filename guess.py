import random
num = random.randint(1, 100)
guess = int(input("Enter any number 1 to 100 : "))
if guess > num:
    print("Too high")
elif guess < num:
    print("Too low")
else:
    print("Correct guess")
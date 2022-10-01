
charge = 0

while True:

    guess = input()
    if guess == 'break':
        break

    if guess <= 2:
        charge = int(guess) + 0
    elif guess >2 and guess <= 12:
        charge = int(guess) + 14
    elif guess >12 and guess < 65:
        charge = int(guess) + 23
    else:
        charge = int(guess) + 18

print(f"{charge:.2f}")

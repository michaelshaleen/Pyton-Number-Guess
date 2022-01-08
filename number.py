import random


def guess(x):
  random_number = random.randint(1, x)
  guess = 0



  while guess != random_number:
    guess = int(input(f"Guess a number between 1 an {x}: "))
    if guess < random_number:
      print("Ha, your guess is lower than the number. Too low")
    elif guess > random_number:
      print("whoops, too high this time.")
  print(f"Huzzah, you guessed the correct number {random_number}")



def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':
    if low != high:
        guess = random.randint(low, high)
    else:
        guess = low
    feedback = input(f"Is {guess} too high (H), or too low (L), or correct (C)?").lower()
    if feedback == 'h':
      high = guess - 1 
    elif feedback == 'l':
      high = guess + 1
  print(f'The Computer guessed your number, {guess}, correctly!')


# out of while loop
computer_guess(10)
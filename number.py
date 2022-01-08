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




# out of while loop
guess(10)
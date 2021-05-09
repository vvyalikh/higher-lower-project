from game_data import data
import random
from replit import clear

def get_random_account(data):
  """Get data from random account"""
  return random.choice(data)

def account_info(choice):
  """Takes account data, returns it in a printable format"""
  account_name = choice["name"]
  account_description = choice["description"]
  account_country = choice["country"]
  return f"{account_name} , {account_description}, from {account_country}"

def check_answer(guess, followers_a, followers_b):
  """Takes user guess, compares with A and B, checks the answer"""
  if a_follower_count > b_follower_count:
    return made_choice == 'a'
  else:
    return made_choice == 'b'

continue_game = True
score = 0
choice_b = get_random_account(data)
choice_a = get_random_account(data)

while continue_game:
  choice_a = choice_b
  choice_b = get_random_account(data)

  while choice_a == choice_b:
    choice_b = get_random_account(data)

  print(f"Account A: {account_info(choice_a)}")
  a_follower_count = choice_a['follower_count']
  #print(a_follower_count)
  print(f"Against account B: {account_info(choice_b)}")
  b_follower_count = choice_b['follower_count']
  #print(b_follower_count)

  made_choice = input("Who has more followers 'A' or 'B':\n").lower()
  clear()
  is_correct = check_answer(made_choice, a_follower_count, b_follower_count)
  if is_correct:
      score += 1
      print(f"Correct! Current score: {score}.")
  else:
      continue_game = False
      print(f"Ups! You loose. Final score: {score}")














  
 






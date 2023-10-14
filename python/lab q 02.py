# Create a Python word-guessing game where the program has a predefined list of
# 5 words. The player is prompted to input a keyword, and the program searches
# the list for a match. Starting with 10 points, each incorrect guess deducts 2
# points. If the player guesses the keyword correctly, the program displays
# congratulations and the final points. When points hit 0, a "try again"
# message is shown.

import random

# Define a list of 5 words
words = ["apple", "banana", "cat", "dog", "house"]

# Generate a random word from the list
word = random.choice(words)

# Set the initial number of points
points = 10

# Print the welcome message
print("Welcome to the word-guessing game!")

# Prompt the player to enter a keyword
keyword = input("Enter a keyword: ")

# Check if the keyword is correct
if keyword == word:
  # Display congratulations and the final points
  print("Congratulations! You guessed the keyword correctly.")
  print("Your final points are:", points)
else:
  # Deduct 2 points for each incorrect guess
  points -= 2

  # Check if the player has any points remaining
  if points > 0:
    # Prompt the player to try again
    print("Incorrect guess. You have", points, "points remaining.")
    print("Try again: ")

    # Get the player's next guess
    keyword = input("Enter a keyword: ")

    # Check if the keyword is correct
    if keyword == word:
      # Display congratulations and the final points
      print("Congratulations! You guessed the keyword correctly.")
      print("Your final points are:", points)
  else:
    # Display the "try again" message
    print("You have 0 points remaining. Try again next time!")

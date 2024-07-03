import random

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
   'coyote crow deer dog donkey duck eagle ferret fox frog goat '
   'goose hawk lion lizard llama mole monkey moose mouse mule newt '
   'otter owl panda parrot pigeon python rabbit ram rat raven '
   'rhino salmon seal shark sheep skunk sloth snake spider '
   'stork swan tiger toad trout turkey turtle weasel whale wolf '
   'wombat zebra ').split()

word_chosen = random.choice(words)

def art(lives):
  HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
  HANGMANPICS = HANGMANPICS[::-1]
  print(HANGMANPICS[lives])


def guess(word):
  lives = 6
  guesser = len(word)*'_'
  while True:  
    guess = input("\nChoose a letter: ")
    while len(guess) > 1 or guess in guesser:
      guess = input("Make sure to enter 1 letter and not repeat guesses: ")
    guess = guess.lower()
    if guess in word:
      print("Correct!")
      for i in range(len(word)):
        if word[i] == guess:
          guesser = guesser[:i] + guess + guesser[i + 1:]
      if '_' not in guesser:
        print(f"You won with {lives} lives left.")
        break
      print(guesser)
    else:
      print("Nope, not in there.")
      lives -= 1
      art(lives)
      if lives == 0:
        print("You lost!")
        print("The word was " + word)
        break
      print(f"{lives} left.")

print("🌟Hangman🌟")
art(6)
guess(word_chosen)
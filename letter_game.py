#This program is going to be similar to our number guessing game. But based on Hang Man. When we're done, we'll a have gave a game that pick a random owrds from a list and then let's us guess letters until we either get all of the letters in the word or run out of chances.

#So first we need to import the random library again.
import random

#Then we need to make a list of words 
words = [
  'apple',
  'banana',
  'orange',
  'coconut',
  'strawberry',
  'lime',
  'grapefruit',
  'lemon',
  'kumquat',
  'blueberry',
  'melon'
]

#So now we need to make our game loop and just like before we're gonna start with while True.
while True:
  
  #I want to let people to quit the game early so let's start the game with an input.
  start = input("Press enter/return to start, or enter Q to quit.")
  #If the user type q or Q this will stop or break the program. Start.lower convert the user input to lowercase q. Even if tbey type uppercase letter.
  if start.lower() == "q":  
    break
  
  
  
  #Now let's pick a random word/number
  #The choice function what it does is it picks a random thing out of an iterable. So you could give it a word and have it pick a random letter out of that word, you could whatever and in this case, 'were gonna have it pick a word out of our list of words.
  secret_word = random.choice(words)
  
  #Let's add more list here:
  #These two lists are gonna hold on to the letters that our users guess. Some of them are gonna be bad because they're not actual letters in the words that we're looking for and some of them are gonna be good because they are letters in the words.
  
  bad_guesses = []
  good_guesses = []
  
  
  #Now I want to be able to limit the number of guesses to 7 guesses, bad guesses. They can miss 7 times. We used a new key word here called "and".
  #So bad_guesses has to be less than 7  things long, and good_guesses and secret_word can't be the same length.
  #The reason why we are comparing good_guesses and secret_word is because all of the letters in good_guesses and all the letters in secret_word should be the same.
  while len(bad_guesses) < 7 and len(good_guesses) != len(secret_word):
    #draw spaces.
    #draw guessed letters, spaces, and strikes 
    for letter in secret_word:
      if letter in good_guesses:
        #Note what the  end='' does is it lets print multiple times on the same line. So we can print each letter next to each other but we're only printing one letter at a time.
        print(letter, end='')
      else:
        print('_', end='')
    #Here we just print a blank line.    
    print('')    
    #We're going to print out strike for however many bad_guesses they have.
    print('Strikes: {}/7'.format(len(bad_guesses)))
    #Let's just print another blank line just to make things looks a little bit nicer.
    print('')
  
  
    #take guess. So now though, we need to get their guess.
    #Note: we add the .lower in guess input so we're just lower casing it as soon as it comes in. That is good since all of our list are lower case.
    guess = input("Guess a letter: ").lower()
    
    #So let's make sure that the length of their guess is equal to 1.
    if len(guess) != 1:
      print("You can only guess a single letter!")
      #continue for the next step of our loop.
      continue
      #or only one of them has to be true. It doesn't matter if they both true.
    elif guess in bad_guesses or guess in good_guesses:
      print("You've already guesses that letter!")
      continue
    #isalpha(), check to make sure that all of the characters in guess. Guess is a string, so it has multiple characters and make sure that all the characters in guess are letter.  
    elif not guess.isalpha():
      print("You can only guess letters!")
      continue  
      
    #This is when we would find out whether or not their guess is a good_guess. So let's find out.
    #print out win/lose.
    if guess in secret_word:
      good_guesses.append(guess)
      if len(good_guesses) == len(list(secret_word)):
        print("You win!!! The word was {}".format(secret_word))
        break
        #There's not anything else that we're gonna do if it's not in there. We're just gonna move on to the next loop. So we don't have to say like "else continue" because that happens automatically.
      
      #But if it's not in the secret_word, then we want to append the letter that they guessed to bad_guesses.
    else:
        
      bad_guesses.append(guess)
  #Here we want an else to match the while above that will run if they run out of guesses.
  else:
    print("You didn't guess it! My secret word was {}".format(secret_word))
  
  
  
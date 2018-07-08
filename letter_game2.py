#"NEW" We want to be able to clear the screen. To do this we are going to have to import the OS library.
#The OS library lets us use functionality on the system level. On the OS level, so your Operating System.
import os
import random
#Now sys is kind of like OS, it's another module provided by Python. And OS let's us talk to the Operating Sysytem, sys lets us do things with Python itself.
import sys


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


#"NEW" Now this function just clear the screen.
#"NEW" So we are going to make a function called clear.
def clear():
  # "NEW" "nt" which is all the modern Windows. They all report their name as being nt.
  if os.name == 'nt':
    #The we want to call the system level utility cls
    os.system('cls')
    #"NEW" Otherwise so you're on Mac you're on Linux.
  else:
    #"NEW" We want to do the same thing , but instead of cls we want to call clear.
    os.system('clear')
    
    
#"NEW" I want to write a new function for the drawing bits.
  #"NEW" Insert a new function named draw.
  # "NEW" Send bad_guesses, good_guesses, secret_word
def draw(bad_guesses, good_guesses, secret_word):
    # "NEW" First thing we want to do is to clear the screen. 
    clear()
    # "NEW" Second thing we want to do is draw the strikes. And we don't need that first new line exp: print('') because we're going to clear the screen anyway.
    print('Strikes: {}/7'.format(len(bad_guesses)))
  
    print('')
  
  
    #"NEW" Let's print out the bad words as well.
    for letter in bad_guesses:
      print(letter, end=' ')
    #"NEW" Then we are going to print out two returns like pressing enter twice like give me like that kind of thing.  
    print('\n\n')  
  
    for letter in secret_word:
      if letter in good_guesses:
        print(letter, end='')
      else:
        print('_', end='')
    #"NEW" The let's do one more blank line at tge bottom, just in case to give ourselves     #a little bit more room.  
    print('')      
    
 
  #I'm going to write a new function and call it get_guess. And I'm gonna have the       #bad_guesses and good_guesses come in.
def get_guess(bad_guesses, good_guesses):
#Let's add while loop because we want to run this a bunch of time. So this loop will  run automatically so we don't need the continue keyword anymore. You can leave them if want.
    while True:
      guess = input("Guess a letter: ").lower()
      
      if len(guess) != 1:
        print("You can only guess a single letter!")
        #No longer need continue key word. You can leave them in or take them out.
        continue
        
      elif guess in bad_guesses or guess in good_guesses:
        print("You've already guesses that letter!")
        #No longer need continue key word. You can leave them in or take them out.
        continue
      
      elif not guess.isalpha():
        print("You can only guess letters!")
        #No longer need continue key word. You can leave them in or take them out.
        continue  
        
      else:
        return guess
      

#I think there should be a function for playing the while entire game. And that way we can just run that function anytime we want the function to happen. Add an arugment done. That says whether or not we're done playing the game.
def play(done):
  #Let's clear the screen
  clear()
  #Let's get our secret word
  secret_word = random.choice(words)
  #Then we're gonna say bad_guesses an empty list
  bad_guesses = []
  #Then we're gonna say good_guesses an empty list
  good_guesses = []  
    #Let's create a while loop here
  while True:
      #We want to draw our drawing and we're gonna send in our bad_guesses, our good_guesses and our secret_word.
      draw(bad_guesses, good_guesses, secret_word)
      #And then we want to get our guess, so get_guess and again we send in bad_guesses and good_guesses.
      guess = get_guess(bad_guesses, good_guesses)
      
      if guess in secret_word:
        good_guesses.append(guess)
        #We're gonna add a new variable here, and we're gonna callm it "found" and set it to True. What this means is, did we find the word? So right now we're going to assume they've found the word.
        found = True
        #So now to check we do these task below:
        for letter in secret_word:
          if letter not in good_guesses:
            #So go through every letter that's in the secret word. If that letter hasn't been guessed, then set found to False.
            found = False
        #If found is still True then do these task below:    
        if found:
          print("You win!!!!")
          print("The secret word was {}".format(secret_word))
          done = True
      #If there guess was not in the secret word then do these:    
      else:
        bad_guesses.append(guess)
        if len(bad_guesses) == 7:
          draw(bad_guesses, good_guesses, secret_word)
          print("You lost!! :( ")
          print("The secret word was {}".format(secret_word))
          done = True 
      #If we the user done playing the game  ask if they want to play again.  
      if done:
        play_again = input("Play again? Y/n ").lower()
        #If the user doesn't input n
        if play_again != 'n':
          #Then we're not done playing the game. So return False.
          return play(done==False)
        else:
            #So in this case sys.exit lets us exit the game, lets us quit the game.
          sys.exit()

#Define funtion named welcome            
def welcome():
  #Ask user for an input.
  start = input("Press Enter/Return to start or Q to quit ").lower()
  if start == 'q':
    print("Bye!")
    #call system to exit
    sys.exit()
  else:
    return True
            
print('Welcome to Letter Guess!')

done = False
  
while True:
  clear()
  welcome()
  play(done)
  
  
  
  
  
  
  
  
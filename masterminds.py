import random
# This is a copy of the board game "Masterminds"

# First creating a menu
menu_display = f"{40*"#"}\n#{38*" "}#\n#{13*" "}MASTERMINDS!{13*" "}#\n#{38*" "}#\n#{3*" "}[1] Play game{22*" "}#\n#{3*" "}[2] How to play{20*" "}#\n#{38*" "}#\n#{38*" "}#"
print(menu_display)

# This is the string for the instructions
instructions = "# The computer will choose a random    #\n# sequence of 4 numbers                #\n# between 1 and 6. You will have to    #\n# try to guess the correct sequence by #\n# entering for example --> 6125. The   #\n# programm will compare the numbers    #\n# and reply to you whether a number is #\n# correct but in wrong position, or if #\n# it's the correct number and in the   #\n# right position.                      #\n# You have a total of 12 guesses.      #\n"
# Userinput to direct in the menu
menu_input = int(input(f"Choose from menu above: "))
# If Userinput is 2 it displayes the instructions
if menu_input == 2:
    print(menu_display)
    print(instructions)
    menu_input = int(input(f"Press [1] to play the game: "))
# This is the function for the actual game
def masterminds():
    # These arrays are used to save previous guesses from the player to keep track of the combinations used
    player_guesses = []
    player_guesses_digits = []
    player_guesses_position = []
    # This variable is the code the player needs to crack
    mastermind_code = f"{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}"
    # Count is used to keep track of how many guesses the player has
    count = 0
    # This is the loop to keep the game going. Maybe I need to change that later because I started writing this game first
    # without a function, but later decided it's easier to end and start the game with a function
    while menu_input == 1:
        # Keeps adding the number of guesses by iterations
        count += 1
        # Asking for the combination from the player
        guess = input("What's your guess? --> ")
        # Blocking invalid input from the player
        while "0" in guess or "7" in guess or "8" in guess or "9" in guess or 4 != len(guess):
            print("Input wrong. Guess can only contain numbers from 1 to 6, and need to be 4 digits long.")
            guess = input("What's your guess? --> ")
        # Index is the position in the combination to check if it's equal to the position of a digit in a guess
        # Both counts are to count how many digits are correct or how many digits are
        index = 0
        count_correct_digit = 0
        count_correct_position = 0
        # This loop is first checking if a digit is correct and in the right position, if not it checks if the digit is at least in the mastermind code
        for digit in guess:
            if digit == mastermind_code[index]:
                count_correct_position += 1
            elif digit in mastermind_code:
                count_correct_digit += 1
            index += 1
        # After checking the digits they guess and amount of correct positions/digits are added to arrays
        player_guesses.append(guess)
        player_guesses_position.append(count_correct_position)
        player_guesses_digits.append(count_correct_digit)
        # Resetting the index again for the next loop
        index = 0
        # Looping through all player guesses to render them to an output
        for sequence in player_guesses:
            print(f"#{7*" "}[ {sequence[0]} ] [ {sequence[1]} ] [ {sequence[2]} ] [ {sequence[3]} ]{8*" "}# Correct digits: {player_guesses_digits[index]} ; Correct positions: {player_guesses_position[index]}")
            index += 1
        # This comparison is checking if the player won, and if yes - it breaks the loop and therefore ends the game
        if count_correct_position == 4:
            print("######### YAY, YOU WON MASTERMINDS! ##########")
            break
        # This comparison is checking if the player is exceeding the amount of tries, if True - it breaks the loop and loses the game
        if count == 12:
            print("######### GAME OVER, YOU LOST ##########")
            break

# Checks if the User chose "Play game" in the menu
if menu_input == 1:
    masterminds()
# This is asking the player if he wants to play again
restart = input("Play again? y/n\n----> ")
# Checking the input, so that the player needs to send an input again if restart does not equal y or n
while restart != "y" and restart != "n":
    print("Wrong input. Try again.")
    restart = input("Play again? y/n\n----> ")
# Restarts the game if User chose y, or else ends it if the user chose n
if restart == "y":
    masterminds()
else:
    print("Thanks for playing!")


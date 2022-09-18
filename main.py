# We import the module to work with system funtions
import os
# We import the module to work with system funtions
import sys
# We import the module to work with random numbers
import random
# We make a banner
Banner = """
=========
    +---+
    |   |
    O   | JailerPY
   /|\  | BE
   / \  | CAREFUL
        | 7w7
=========
"""
# We make the graffics of the games
b = [
"""
=========
    +---+
    |   |
    O   | JailerPY
   /|\  | BE
   / \  | CAREFUL
        | 7w7
=========
""",
"""
=========
    +---+
    |   |
    O   | JailerPY
   /|\  | BE
        | CAREFUL
        | 7w7
=========
""",
"""
=========
    +---+
    |   |
    O   | JailerPY
    |   | BE
        | CAREFUL
        | 7w7
=========
""",
"""
=========
    +---+
    |   |
    O   | JailerPY
        | BE
        | CAREFUL
        | 7w7
=========
""",
"""
=========
    +---+
    |   |
        | JailerPY
        | BE
        | CAREFUL
        | 7w7
=========
"""
]

# We make the main funtion
def main():
    # We show the banner
    print(Banner)
    # We create a infinite bucle
    while True:
        # We list the files
        files = os.listdir()
        # We ask if the player wants to start the game
        input("Press any button to start...")
        # We clear the screen
        os.system("cls")
        # We select a file
        name_file = list(files[random.randint(0, len(files))-1])
        # We measure the word
        lenght_file = len(name_file)
        # We make a variable to remember the lives of the player
        lives = 4
        # Status of the player
        status = False
        # We hide the word
        hide_word = list(("_"*lenght_file))
        # We create a bucle for the game...
        while lives >= 0 and status == False:
            # Show an imagen
            print(b[lives])
            # Show the name of the file
            print(" ".join(hide_word)+"\n")
            # We request a letter
            letter = input("Write a letter... ")
            # if the letter is in the word
            if letter in name_file:
                # We go through the word
                for l in range(len(name_file)):
                    # If the variable is same to letter then...
                    if name_file[l] == letter:
                        # We replace the letter in the hide word
                        hide_word[l] = letter
                        # Check if the gamer win
                        if "_" not in hide_word:
                            # We clear the screen
                            os.system("cls")
                            # Show the name of the file
                            print(" ".join(hide_word))
                            # Show a message and wait
                            input("""             ____
            / . .\\
You Safe    \  ---<
Your File!!  \  /
   __________/ /
-=:___________/
Press any button to continue...""")
                            # We change the status of the player
                            status = True
            # And if not...
            else:
                # We subtract a live
                lives -= 1
                # If the player doesnt have any lives...
                if lives < 0:
                    # We show a message
                    input("You lost the file: {}".format("".join(name_file)))
                    # We open the file...
                    with open("".join(name_file), "w") as document:
                        # We write some in the document
                        document.write("RIP")
            # We clear the screen
            os.system("cls")
# We make a access point
if __name__ == '__main__':
    # We try to execute the next code...
    try:
        # We call the main funtion
        main()
    # If we have an error then...
    except KeyboardInterrupt as e:
        # We dont execute any code
        sys.exit()

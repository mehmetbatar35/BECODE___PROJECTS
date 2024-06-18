import random
from typing import List

class Hangman:

    """
    A class used to represent a Hangman game.

    Attributes
    ----------
    possible_words : list
        a list of possible words to be guessed
    word_to_find : list
        the word to be guessed, chosen randomly from possible_words
    lives : int
        the number of lives the player has
    correctly_guessed_letters : list
        a list representing the correctly guessed letters
    wrongly_guessed_letters : list
        a list representing the wrongly guessed letters
    turn_count : int
        the number of turns taken by the player
    error_count : int
        the number of errors made by the player

    Methods
    -------
    play():
        Handles the logic for a single turn of the game.
    start_game():
        Starts the game and continues until the player wins or loses.
    game_over():
        Prints a game over message with the correct word.
    well_played():
        Prints a congratulatory message with the game's statistics.
    """

    def __init__(self):

        """
        Initializes the Hangman game with a list of possible words,
        selects a word randomly, and sets the initial state of the game.
        """
        
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters = []  
        self.turn_count = 0
        self.error_count = 0




    def play(self):
                
        """
        Handles the logic for a single turn of the game.
        Prompts the player to enter a letter and updates the game state accordingly.
        """

        print("************************************************************")
        letter = input("Enter a letter: ").lower()
        self.turn_count += 1
        if not letter.isalpha() or len(letter) != 1:
            print(f"{letter} is invalid input. Please enter a single letter.")
            return
        if letter in self.word_to_find:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    self.correctly_guessed_letters[i] = letter
        else:
            if letter in self.wrongly_guessed_letters:
                print(f"You have already guessed {letter}. Please try another letter.")
                return
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1

    def start_game(self):

        """
        Starts the game and continues until the player wins or loses.
        Displays the current state of the game after each turn.
        """

        while self.lives > 0 and "_" in self.correctly_guessed_letters:
            self.play()
            print(f"Correctly guessed letters: {self.correctly_guessed_letters}")
            print(f"Wrongly guessed letters: {self.wrongly_guessed_letters}")
            print(f"Lives left: {self.lives}")
            print(f"Turn count: {self.turn_count}")
            print(f"Error count: {self.error_count}")

            if self.lives == 0:
                self.game_over()
            elif "_" not in self.correctly_guessed_letters:
                self.well_played()
                
    def game_over(self):

        """
        Prints a game over message with the correct word.
        """

        print(f"Game over. The correct word was {self.word_to_find}")

    def well_played(self):

        """
        Prints a congratulatory message with the game's statistics.
        """

        print(f"Congratulations! You have found the correct word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors.")
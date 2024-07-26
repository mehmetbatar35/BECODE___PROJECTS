import random
import streamlit as st

class Hangman:
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def get_display_word(self):
        return " ".join(self.correctly_guessed_letters)    

    def play(self, letter):
        if not letter.isalpha() or len(letter) != 1:
            st.session_state.warning_message = f"{letter} is invalid input, please enter a single letter."
            return

        self.turn_count += 1

        if letter in self.word_to_find:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    self.correctly_guessed_letters[i] = letter

        elif letter in self.wrongly_guessed_letters:
            st.session_state.warning_message = f"You have already guessed {letter}. Please try another letter."
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1            
            self.lives -= 1

    def start_game(self):
        st.write(f"Correctly guessed letters: {self.get_display_word()}")
        st.write(f"Wrongly guessed letters: {', '.join(self.wrongly_guessed_letters)}")
        st.write(f"Lives left: {self.lives}")
        st.write(f"Turn count {self.turn_count}")
        st.write(f"Error count: {self.error_count}")

        if self.lives == 0:
            st.error(f"Game over. The correct word was: {''.join(self.word_to_find)}")
            st.stop()
        elif "_" not in self.correctly_guessed_letters:
            st.success(f"Congratulations! You have found the correct word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors.")
            st.stop()

if 'game' not in st.session_state:
    st.session_state.game = Hangman()
if 'warning_message' not in st.session_state:
    st.session_state.warning_message = ""

st.title("Hangman Game")     
st.session_state.game.start_game()

if st.session_state.warning_message:
    st.warning(st.session_state.warning_message)
    st.session_state.warning_message = ""

guess = st.text_input("Enter a letter: ").lower()
st.write(f"Debug: Current input is '{guess}'")

if st.button("Guess"):
    if guess and len(guess) == 1 and guess.isalpha():  
        st.session_state.game.play(guess)
        st.experimental_rerun()
    else:
        st.session_state.warning_message = "Please enter a single letter before clicking 'Guess'."
        st.experimental_rerun()
def get_word():

    """
    Prompts the user to enter a word.

    Returns
    -------
    str
        The word entered by the user.
    """

    word = input("Enter your word: ")
    return word

def get_lives():

    """
    Prompts the user to enter the number of lives.

    Returns
    -------
    int
        The number of lives entered by the user.
    """

    while True:
        try:
            return int(input("Enter you number of lives: "))
        except ValueError:
            print("Please enter a valid number of lives.")


def get_guess(suggested_letters):

    """
    Prompts the user to enter a letter and checks if it has been guessed before.

    Parameters
    ----------
    suggested_letters : list
        The list of letters that have been suggested already.

    Returns
    -------
    str
        The guessed letter.
    """

    while True:
        letter = input("Enter a letter: ")
        if len(letter) != 1:
            print(f"{letter} has {len(letter)}. But it should be only one letter.")
            letter = input("Enter a letter: ")
        elif letter in suggested_letters:
            print(f"You have already suggested {letter} letter. So please try another letter.")            
        else:
            suggested_letters.append(letter)
            return letter    
        


def assess_guess(secret_word, guessed_letter, lives_left):

    """
    Checks if the guessed letter is in the secret word and updates the number of lives left.

    Parameters
    ----------
    secret_word : str
        The word to be guessed.
    guessed_letter : str
        The letter guessed by the user.
    lives_left : int
        The number of lives left.

    Returns
    -------
    int
        The updated number of lives left.
    """

    if guessed_letter in secret_word:
        print(f"{guessed_letter} is correct guess.")
        return lives_left
    else:
        print(f"{guessed_letter} is NOT correct guess.")
        lives_left -= 1
        return lives_left
    



def display_word(secret_word, suggested_letters):

    """
    Displays the current state of the word being guessed, with correctly guessed letters and underscores for others.

    Parameters
    ----------
    secret_word : str
        The word to be guessed.
    suggested_letters : list
        The list of letters that have been guessed.

    Returns
    -------
    bool
        True if the entire word has been guessed, False otherwise.
    """

    displayed_word = ""
    for i in secret_word:
        if i in suggested_letters:
            displayed_word += i + ' '
        else:
            displayed_word += "_"    
    print(displayed_word)
    if "_" not in displayed_word:
        return True
    else:
        return False 

def main():

    """
    The main function to run the Hangman game.
    """
    
    secret_word = get_word()
    lives_left = get_lives()        
    suggested_letters = []
    correct = False

    while lives_left > 0 and not correct:
        print(f"Lives left: {lives_left}, type of lives: {type(lives_left)}")
        guess = get_guess(suggested_letters)
        suggested_letters.append(guess)
        lives_left = assess_guess(secret_word, guess, lives_left)
        correct = display_word(secret_word, suggested_letters)

    if correct:
        print(f"Congratulations! You have found the correct word: {secret_word}")
    else:
        print(f"Game over. The correct word was {secret_word}")    

main() 

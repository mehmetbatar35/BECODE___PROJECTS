import random


def generate_random_number():
    return random.randint(1, 100)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def play_game():
    print("Who wants to play 'Guess the Number' game: ", end = "")
    my_name = input()
    random_num = generate_random_number()
    attempt = 0
    while attempt < 10:
        attempt += 1
        guess = input("Enter your guess: ")
        if is_integer(guess):
            guess = int(guess)
            if 1 <= guess <= 100:
                if guess > random_num:
                    print(f"Your guess is too high {my_name}. You have still {10 - attempt} attempts.")
                elif guess < random_num:
                    print(f"Your guess is too low {my_name}. You have still {10 - attempt} attempts.")
                else:
                    print(f"Congratulations {my_name}! Your guess is correct. You can find it in your {attempt}. attempt.")
                    return
            else:
                print(f"Your guess is out of range {my_name}. Please enter a number between 1 and 100. You have still {10 - attempt} attempts")
        else:
            print(f"Error: Your guess is not a digit {my_name}. Please enter a valid integer. You have still {10 - attempt} attempts")
            
    print("You didn't find it {}. The correct answer was {}.".format(my_name, random_num))        
            
play_game()         













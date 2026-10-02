
from modules import request_word_from_api

print(f"Welcome to Hangman!")

categories = ['animals', 'birds', 'capitals_of_countries', 'countries', 'wordle', 'sports']
indexes = ['1', '2', '3', '4', '5', '6']
lengths = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'any']
answer = ''

while True:
    while True:
        print('1 - Animals | 2 - Birds | 3 - Capitals of Countries | 4 - Countries | 5 - Wordle | 6 - Sports')
        category_number = (input("Choose a category: \n"))
        if category_number in indexes:
            idx = int(category_number)
            category = categories[idx-1]
            break
    while True:
        word_length = (input("Length of word: (4 - 20) or any (any length) \n"))
        if word_length in lengths:
            break

    answer = request_word_from_api(category, word_length)
    if answer is not None:
        break

body_parts = ['O', '|', '/', '\\', '/', '\\']
print_body_parts = [' ', ' ', ' ', ' ', ' ', ' ']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lives_left = 6
word_to_guess = answer
word_to_guess_list = ['_' for _ in range(len(word_to_guess))]
for index, letter in enumerate(word_to_guess):
    if letter == ' ':
        word_to_guess_list[index] = " "
game_play = True

while game_play:

    game_interface = f"""
          +-----+
          |     |     Letter Bank
          {print_body_parts[0]}     |       {" ".join(alphabet)}
        {print_body_parts[2]} {print_body_parts[1]} {print_body_parts[3]}   |
         {print_body_parts[4]} {print_body_parts[5]}    |
                |     ***** {lives_left} / 6 lives left *****
       -----------      
    """

    word_to_guess_line = f"Word to guess: {' '.join(word_to_guess_list)}"
    print(game_interface)
    print(word_to_guess_line)

    if ''.join(word_to_guess_list) == word_to_guess.upper():
        print('Congradulations, You won!')
        game_play = False
    elif lives_left == 0:
        print(f'The word was {word_to_guess}. You are out of lives! Game over')

        game_play = False
    else:
        while True:
            user_guess = input("Guess a letter: ")
            if user_guess.upper() not in alphabet:
                print(f"You already guessed {user_guess.upper()}. Try again.")
            else:
                break

        if user_guess.lower() in word_to_guess:
            position = alphabet.index(user_guess.upper())
            alphabet[position] = " "
            for index, letter in enumerate(word_to_guess):
                if letter == user_guess:
                    word_to_guess_list[index] = user_guess.upper()
        else:
            print(f'{user_guess} is not in the word. Try again!')
            lives_left -= 1
            position = alphabet.index(user_guess.upper())
            alphabet[position] = " "
            print_body_parts[6 - lives_left - 1] = body_parts[6 - lives_left - 1]

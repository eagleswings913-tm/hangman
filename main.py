
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
            print(categories[idx-1])
            category = categories[idx-1]
            break
    while True:
        word_length = (input("Length of word: (4 - 20) or any (any length) \n"))
        if word_length in lengths:
            break

    answer = request_word_from_api(category, word_length)
    print(f'Answer: {answer}')
    if answer is not None:
        break



body_parts = ['O', '|', '/', '\\', '/', '\\']
print_body_parts = [' ', ' ', ' ', ' ', ' ', ' ']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
word_to_guess = "brave"
word_to_guess_list = ['_' for _ in range(len(word_to_guess))]

game_interface = f"""
      +-----+
      |     |     Letter Bank
      {print_body_parts[0]}     |       {" ".join(alphabet)}
    {print_body_parts[2]} {print_body_parts[1]} {print_body_parts[3]}   |
     {print_body_parts[4]} {print_body_parts[5]}    |
            |     ***** 6 / 6 lives left *****
   -----------      
"""
word_to_guess_line = f"Word to guess: {' '.join(word_to_guess_list)}"

print(game_interface)
print(word_to_guess_line)

user_guess = input("Guess a letter:")
import random

COMBINATION_LENGTH = 4
MAX_ATTEMPTS = 10

COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']

CORRECT_POSITION = '+'
CORRECT_COLOR = '='

MESSAGE_VICTORY = "Félicitations ! Vous avez réussi."
MESSAGE_DEFEAT = "Dommage, vous avez perdu"
MESSAGE_PROMPT = "Allez-y Choisisez une combinaison de 4 couleurs "
MESSAGE_ERROR = "Combinaison invalide. Assurez-vous d'utiliser les couleurs valides et d'avoir la bonne longueur de 4 couleur."


def generate_secret_combination():
    
    return random.choices(COLORS, k=COMBINATION_LENGTH)

def get_player_guess():
    
    input_guess = input(MESSAGE_PROMPT).upper().strip().split()
   
    if len(input_guess) != COMBINATION_LENGTH or not all(char in COLORS for char in input_guess):
        print(MESSAGE_ERROR)
        return get_player_guess()
    return input_guess

if __name__ == "__main__":
    secret_combination = generate_secret_combination()
    print("Combinaison secrète générée :", secret_combination)

    player_guess = get_player_guess()
    print("Proposition du joueur :", player_guess)

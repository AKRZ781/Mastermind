import random

# Constantes
COMBINATION_LENGTH = 4
MAX_ATTEMPTS = 10
COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']
CORRECT_POSITION = '='  
CORRECT_COLOR = '+'  
WRONG = '*'  

# Messages
MESSAGE_VICTORY = "🎉 Félicitations ! Vous avez réussi en {attempts} tentatives."
MESSAGE_DEFEAT = "😢 Dommage, vous avez perdu. La combinaison secrète était : {secret_combination}"
MESSAGE_PROMPT = "Allez-y, choisissez une combinaison de 4 couleurs (ex: R G B Y) : "
MESSAGE_ERROR = "❌ Combinaison invalide. Assurez-vous d'utiliser les couleurs valides et d'avoir la bonne longueur de 4 couleurs."
MESSAGE_INTRO = """
Bienvenue dans le jeu Mastermind ! 
Votre objectif est de deviner une combinaison secrète de {length} couleurs parmi les suivantes :
{colors}
- {correct_position} : Bonne couleur, bonne position.
- {correct_color} : Bonne couleur, mauvaise position.
- {wrong} : Mauvaise couleur.
Vous avez {max_attempts} tentatives. Bonne chance !
"""

def generate_secret_combination():
    return random.choices(COLORS, k=COMBINATION_LENGTH)

def get_player_guess():
    input_guess = input(MESSAGE_PROMPT).upper().strip().split()
    if len(input_guess) != COMBINATION_LENGTH or not all(char in COLORS for char in input_guess):
        print(MESSAGE_ERROR)
        return get_player_guess()
    return input_guess

def check_guess(secret_combination, player_guess):
    result = [WRONG] * COMBINATION_LENGTH
    secret_used = [False] * COMBINATION_LENGTH
    guess_used = [False] * COMBINATION_LENGTH

    for i in range(COMBINATION_LENGTH):
        if player_guess[i] == secret_combination[i]:
            result[i] = CORRECT_POSITION
            secret_used[i] = True
            guess_used[i] = True

    for i in range(COMBINATION_LENGTH):
        if not guess_used[i]:
            for j in range(COMBINATION_LENGTH):
                if not secret_used[j] and player_guess[i] == secret_combination[j]:
                    result[i] = CORRECT_COLOR
                    secret_used[j] = True
                    break

    return ''.join(result)

def play_game():
    secret_combination = generate_secret_combination()
    print(MESSAGE_INTRO.format(
        length=COMBINATION_LENGTH,
        colors=" ".join(COLORS),
        correct_position=CORRECT_POSITION,
        correct_color=CORRECT_COLOR,
        wrong=WRONG,
        max_attempts=MAX_ATTEMPTS
    ))

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"\nTentative {attempt}/{MAX_ATTEMPTS}")
        player_guess = get_player_guess()
        result = check_guess(secret_combination, player_guess)

        print(f"Votre proposition : {' '.join(player_guess)}")
        print(f"Résultat         : {result}")

        if result.count(CORRECT_POSITION) == COMBINATION_LENGTH:
            print(MESSAGE_VICTORY.format(attempts=attempt))
            break
    else:
        print(MESSAGE_DEFEAT.format(secret_combination=" ".join(secret_combination)))

if __name__ == "__main__":
    play_game()

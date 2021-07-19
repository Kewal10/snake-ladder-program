import random
import time



board_size = 100
max_steps = 10
crooked_dice = False
player_name = "Player 1"
sleep_time = 0.5

snakes = {
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

ladders = {
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}
def welcome_msg():
    msg = """
***********************************************************************************
*               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>              *
*               ^                                                  ^              *
*               ^ Welcome to Snake ~~~~~> and Ladder ####### Game  ^              *
*               ^                                                  ^              *
*               ####################################################              *
*          _____________________________________________________________          *
*         |                                                             |         *
*         |      Rules:                                                 |         *
*         |      1. Initally player(s) starts at 0.                     |         *
*         |          dice will be rolled each turn, Moving the player   |         * 
*         |          forward the number of spaces shown on the dice.    |         *
*         |      2. If you lands at the bottom of a ladder,             |         *
*         |          you climb to the top of the ladder.                |         *
*         |      3. If you lands on the head of a snake,                |         *
*         |          you fall down to the bottom of the snake.          |         *
*         |      4. If player gets to the FINAL position                |         *
*         |          he will be declared the winner.                    |         *
*         |                                                             |         *
*         |      This game will run for """+str(max_steps)+""" steps                        |         *
*         |      Press <enter> to start game                            |         *
*         |                                                             |         *
*         |_____________________________________________________________|         *
*                                                                                 *
*                                                                                 *
*                                                                                 *
***********************************************************************************
\n"""

    return input(msg).strip()




def role_dice():
    time.sleep(sleep_time)
    steps = random.randint(1, 6)
    if crooked_dice == True:
        if (steps % 2 != 0):
            steps += 1
    print("\n" +"The dice tuned to be [" + str(steps)+"]")
    return steps


def process_steps(player_name,current_position,steps):
    time.sleep(sleep_time)
    old_position = current_position
    current_position = current_position + steps

    if current_position > board_size:
        print("You need " + str(board_size - old_position) + " to win this game. Keep trying.")
        return old_position

    print("\n" + player_name + " moved from " + str(old_position) + " to " + str(current_position))
    if current_position in snakes:
        final_position = snakes.get(current_position)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~ SNAKE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~> "+ "\n" + player_name + " got a snake bite :'( Falling from " + str(current_position) + " to " + str(final_position))

    elif current_position in ladders:
        final_position = ladders.get(current_position)
        print("######################### Ladder ############################ " + "\n" + player_name + " Going Up B-) from " + str(current_position) + " to " + str(final_position))

    else:
        final_position = current_position

    return final_position


def check_winner(player_name, position):
    time.sleep(sleep_time)
    if board_size == position:
        print("\n\n\nHe have a WINNERR!!!!.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        return True



def main():
    player_input = welcome_msg()
    time.sleep(sleep_time)
    if player_input.lower() == "crooked":
        print("\n***********************************************************************************\n You have unlocked the Crooked Dice that only throws Even numbers! ;-)\n***********************************************************************************\n")
        global crooked_dice
        crooked_dice = True
    player1_position = 0

    # while True:
    for i in range(max_steps):
        steps = role_dice()
        time.sleep(sleep_time)
        player1_position = process_steps(player_name, player1_position, steps)
        time.sleep(sleep_time)
        if check_winner(player_name,player1_position):
             break
        print("\n====================================================================")
    print("Game Over!! \n====================================================================")

if __name__ == '__main__':
    main()
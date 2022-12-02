from day2_input import input_rows

SAMPLE_INPUT = [['A', 'Y'], ['B', 'X'],['C', 'Z']]

LEFT_PLAY_MAP = {'A': 1, 'B': 2, 'C': 3}
LEFT_PLAY_MAP_REVERSED = {v: k for k, v in LEFT_PLAY_MAP.items()}
RIGHT_PLAY_MAP = {'X': -1, 'Y': 0, 'Z': 1}

def get_game_winner_points(left_choice, right_choice):
    result = left_choice - right_choice
    if result == 0:
        return 3
    elif result == 1 or result == -2:
        return 0
    else:
        return 6

#I guess I already unmapped this
def get_play_points(play):
    return play


def get_correct_play(left_play, my_result):
    my_score = left_play + my_result
    if my_score == 0:
        my_score += 3
    elif my_score == 4:
        my_score -= 3
    return LEFT_PLAY_MAP_REVERSED[my_score]
    

def get_game_total_points(game):
    left_player_choice = LEFT_PLAY_MAP[game[0]]
    right_player_letter = get_correct_play(left_player_choice, RIGHT_PLAY_MAP[game[1]])
    right_player_choice = LEFT_PLAY_MAP[right_player_letter]
    return get_game_winner_points(left_player_choice, right_player_choice) + get_play_points(right_player_choice)


###
# For each input row, the first column is the opponent play
# and the second column is whether I need to win, lose, or draw
def main(input_rows):
    my_game_points = 0
    for game in input_rows:
        my_game_points += get_game_total_points(game)
    print(my_game_points)
    return my_game_points


if __name__ == "__main__":
    main(input_rows)

def score(game):
    """ 
    Calculates the total score of a bowling game.
    """
    score = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            last = get_value(game[i-1])
            score += 10 - last
        else:
            score += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                score += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                score += get_value(game[i+1])
                if game[i+2] == '/':
                    score += 10 - get_value(game[i+1])
                else:
                    score += get_value(game[i+2])
        if not in_first_half:
            frame += 1
            in_first_half = True
        else:
            in_first_half = False
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    return score


def get_value(char):
    """
    Returns the value of the actual roll
    """

    if '1' <= char <= '9':
        return int(char)
    elif char in ["x", "X", "/"]:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

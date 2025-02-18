import random
import time
from collections import deque

def you_win(my_pick, score):
    score += 100
    print(f"Well done. The computer chose {my_pick} and failed")
    return score

def I_win(my_pick):
    print(f"Sorry, but the computer chose {my_pick}")

def draw(my_pick, score):
    score += 50
    print(f"It's a draw ({my_pick})")
    return score

def bye(score):
    data_string = ""
    for score in data:
        """
        Convert the list of lists to a string
        """
        data_string += score[0] + " " + score[1] + "\n"
    data_string = data_string[:-1]  # ...and tidy up.

    test = open("rating.txt", "w")
    test.write(data_string)  # Save the scores
    test.close()

    print("Bye!")

def winnersAndLosers(game, pick):
    """
    :param game: The list of tge game's options
    :param pick: The player's pick; always Spock if you're one of the Big Bang boys!
    :return: Two lists of winning and losing picks
    """
    offsets = len(game) // 2
    recentered = deque(game)
    recentered.rotate(offsets - game.index(pick))  # Game, but symmetric about the player's choice
    beats = []
    loses_to = []
    for i in range(1, offsets + 1):
        beats.append(recentered[offsets + i])
        loses_to.append(recentered[offsets - i])
    return beats, loses_to

if __name__ == "__main__":

    player = input("Enter your name: ")
    print(f"Hello, {player}")
    """
    Get the scores from the file
    """
    test = open("rating.txt", "r")
    lines = test.readlines()
    test.close()

    data = []
    for line in lines:
        """
        Create a list of lists
        [[player1, score1], [player2, score2], ...]
        """
        data.append(line.split())

    if player not in sum(data, []):
        data.append([player, "0"])  # Add the new player if not already present

    for scores in data:
        """
        Get the player's score
        """
        if scores[0] == player:
            score = int(scores[1])

    """
    Set up the game
    """
    game = input()
    if game:
        game = game.lower().split(",")
    else:
        game = ['rock', 'paper', 'scissors']

    print("Okay, let's start")

    random.seed(int(time.time()))  # Otherwise, the computer always picks rock!

    continue_playing = True

    while continue_playing:
        pick = input().lower()
        my_pick = random.choice(game)

        if pick in game:  # A game choice or something else?
            winners, losers = winnersAndLosers(game, pick)
        else:
            winners, losers = [], []

        if pick == "!rating":
            print(f"Your rating: {score}")
        elif pick == "!exit":
            bye(score)
            continue_playing = False
        elif my_pick in winners:
            I_win(my_pick)
        elif my_pick in losers:
            score = you_win(my_pick, score)
        elif my_pick == pick:
            score = draw(my_pick, score)
        else:
            print("Invalid input")

        for scores in data:
            """
            Add the score to the user
            """
            if scores[0] == player:
                scores[1] = str(score)

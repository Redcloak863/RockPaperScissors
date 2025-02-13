import random
import time

def you_win(my_pick):
    print(f"Well done. The computer chose {my_pick} and failed")

def I_win(my_pick):
    print(f"Sorry, but the computer chose {my_pick}")

def draw(my_pick):
    print(f"It's a draw ({my_pick})")

random.seed(int(time.time()))  # Otherwise, the computer always picks rock!

if __name__ == "__main__":

    continue_playing = True

    while continue_playing:
        pick = input().lower()
        my_pick = random.choice(["rock", "paper", "scissors"])

        if pick == "!exit":
            print("Bye!")
            continue_playing = False
        elif pick == "rock":
            if my_pick == "paper":
                I_win(my_pick)
            elif my_pick == "scissors":
                you_win(my_pick)
            else:
                draw(my_pick)

        elif pick == "paper":
            if my_pick == "scissors":
                I_win(my_pick)
            elif my_pick == "rock":
                you_win(my_pick)
            else:
                draw(my_pick)

        elif pick == "scissors":
            if my_pick == "rock":
                I_win(my_pick)
            elif my_pick == "paper":
                you_win(my_pick)
            else:
                draw(my_pick)
        else:
            print("Invalid input")


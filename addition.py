# !/usr/bin/env python3

import playsound
import random
import threading

from internal import format

MAX = 30


def playSound(path: str) -> None:
    thread = threading.Thread(target=playsound.playsound, args=(path,),
        daemon=True)
    thread.start()


def main() -> None:
    random.seed(version=2)

    example = 0
    while True:
        example += 1

        correct_answer = random.randint(0, MAX)
        left = random.randint(0, correct_answer)
        right = correct_answer - left

        print("#" + str(example) + ": " + str(left) + " + " + str(right) + " = ",
            end = '')
        user_string = input()
        if not user_string:
            return

        if user_string.isnumeric():
           answer = int(user_string)
           if (left + right) == answer:
               playSound("media/correct.wav")
               print(format.LIGHT_GREEN + "correct" + format.NC)
               continue

        playSound("media/wrong.wav")
        print(format.RED + "NOT QUITE CORRECT." + format.NC + " try again")


main()

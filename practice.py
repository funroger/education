# !/usr/bin/env python3

# system imports
import argparse
import playsound
import sys
import threading

from internal import console
from internal import format
from internal import platform


# declare parameters names
class ARGS:
    MODULE = "module"


def parse_arguments():
    # initialize argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", help="path to a module file",
       default="", type=str)
    args = parser.parse_args()

    # save actual values
    ctx = {}
    ctx[ARGS.MODULE] = args.module

    return ctx


def play_sound(path: str) -> None:
    thread = threading.Thread(target=playsound.playsound, args=(path,),
        daemon=True)
    thread.start()


def main() -> None:

    console.clear()

    # load module
    ctx = parse_arguments()
    module_path = ctx[ARGS.MODULE]
    if not module_path:
        platform.exit_on_error("specify module to execute")
    module = platform.load_module(module_path)
    if None == module:
        platform.exit_on_error("can't load module " + module_path)

    print("MODULE: " + module.NAME + "\n")
    module.initialize()

    # start practicing
    taskIdx = 0
    while True:
        taskIdx += 1

        task = module.get_task()

        print("#" + str(taskIdx) + ": " + task.Desc(), end = '')
        user_answer = input()
        if not user_answer:
            return

        correct = module.check_task(task, user_answer)

        if correct:
            play_sound("media/correct.wav")
            print(format.LIGHT_GREEN + "correct" + format.NC)
        else:
            play_sound("media/wrong.wav")
            print(format.RED + "NOT QUITE CORRECT." + format.NC)


main()

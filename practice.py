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


__media_threads = []


def play_sound(path: str) -> None:
    thread = threading.Thread(target=playsound.playsound, args=(path,))
    thread.start()
    __media_threads.append(thread)


def run_practice(module, tasks: list) -> list:
    wrong_tasks = []
    taskIdx = 0
    while True:
        # get task and task number
        if len(tasks):
            if taskIdx >= len(tasks):
                break
            taskNum, task = tasks[taskIdx]
        else:
            taskNum = taskIdx + 1
            task = module.get_task()

        # get user input
        while True:
            print("#" + str(taskNum) + ": " + task.Desc(), end = '')
            user_answer = input()
            if user_answer:
                break
            print(format.YELLOW + "Do you want to quit?" + format.NC + " [y/n] ")
            user_answer = input()
            if user_answer == "y":
                return wrong_tasks

        # check results
        correct = module.check_task(task, user_answer)
        if correct:
            play_sound("media/correct.wav")
            print(format.GREEN + "correct" + format.NC)
        else:
            play_sound("media/wrong.wav")
            print(format.RED + "NOT QUITE CORRECT" + format.NC)
            wrong_tasks.append((taskNum, task))

        taskIdx += 1

    return wrong_tasks


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
    wrong_tasks = []
    while True:
        wrong_tasks = run_practice(module, wrong_tasks)

        if not wrong_tasks:
            break

        print(format.YELLOW + "Some answers were not quite correct." + 
            format.NC + " Do you want to correct them? [y/n] ", end = '')
        user_answer = input()
        if not user_answer == "y":
            break

    for thread in __media_threads:
        thread.join()


main()

# !/usr/bin/env python3

import random

NAME = "Simple division [2..11]"

class Task:
    def Desc(self) -> str:
        return self._desc


def initialize() -> None:
    random.seed(version=2)


def get_task() -> Task:
    task = Task()
    task._divisor = random.randint(2, 11)
    task._correct_answer = random.randint(1, 11)
    task._dividend = task._divisor * task._correct_answer
    task._desc = str(task._dividend) + " / " + str(task._divisor) + " = "
    return task


def check_task(task: Task, user_answer: str) -> bool:
    if user_answer.isnumeric():
        answer = int(user_answer)
        if task._correct_answer == answer:
            return True
    return False

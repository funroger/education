# !/usr/bin/env python3

import random

NAME = "Addition [0..100]"

class Task:
    def Desc(self) -> str:
        return self._desc


def initialize() -> None:
    random.seed(version=2)


def get_task() -> Task:
    task = Task()
    task._correct_answer = random.randint(0, 100)
    task._left = random.randint(0, task._correct_answer)
    task._right = task._correct_answer - task._left
    task._desc = str(task._left) + " + " + str(task._right) + " = "
    return task


def check_task(task: Task, user_answer: str) -> bool:
    if user_answer.isnumeric():
        answer = int(user_answer)
        if task._correct_answer == answer:
            return True
    return False

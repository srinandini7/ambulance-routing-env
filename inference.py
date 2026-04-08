import os
from env import AmbulanceEnv
from tasks import task_easy, task_hard, task_medium

print("[START]")

env = AmbulanceEnv()

tasks = [task_easy, task_medium, task_hard]

tasks = [
    ("easy", task_easy),
    ("medium", task_medium),
    ("hard", task_hard),
]

for name, task in tasks:
    print(f"[STEP] task={name}")
    score = task.run(env)
    print(f"[STEP] score={round(score, 2)}")

print("[END]")
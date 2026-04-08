# Objective: Reach patient location
from models import Action

def run(env):
    env.reset()
    total_reward = 0

    for _ in range(10):
        action = Action(move="forward")
        obs, reward, done, _ = env.step(action)
        total_reward += reward

        if done:
            break

    return min(total_reward / 10, 1.0)

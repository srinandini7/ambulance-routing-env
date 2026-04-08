# Objective: Complete full route efficiently within step limit
from models import Action

def run(env):
    obs = env.reset()
    total_reward = 0

    for _ in range(20):
        move = "forward"
        action = Action(move=move)

        obs, reward, done, _ = env.step(action)
        total_reward += reward

        if done:
            break

    return min(total_reward / 20, 1.0)

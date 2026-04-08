# Objective: Reach patient and move toward hospital
from models import Action

def run(env):
    obs = env.reset()
    total_reward = 0

    for _ in range(15):
        move = "forward" if obs.ambulance_location < obs.patient_location else "forward"
        action = Action(move=move)

        obs, reward, done, _ = env.step(action)
        total_reward += reward

        if done:
            break

    return min(total_reward / 15, 1.0)

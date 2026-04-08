from fastapi import FastAPI
from env import AmbulanceEnv
from models import Action

app = FastAPI()
env = AmbulanceEnv()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    obs, reward, done, _ = env.step(action)
    return {"obs": obs, "reward": reward, "done": done}

@app.get("/state")
def state():
    return env.state()
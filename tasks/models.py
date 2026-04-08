from pydantic import BaseModel

class Observation(BaseModel):
    ambulance_location: int
    patient_location: int
    hospital_location: int
    time_elapsed: int

class Action(BaseModel):
    move: str  # "forward" or "backward"
from models import Observation, Action

class AmbulanceEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.ambulance_location = 0
        self.patient_location = 5
        self.hospital_location = 10
        self.time_elapsed = 0
        self.picked = False

        return self._get_obs()

    def step(self, action: Action):
        self.time_elapsed += 1

        # move ambulance
        if action.move == "forward":
            self.ambulance_location += 1
        elif action.move == "backward":
            self.ambulance_location -= 1

        # distances
        distance_to_patient = abs(self.ambulance_location - self.patient_location)
        distance_to_hospital = abs(self.ambulance_location - self.hospital_location)

        reward = 0.0
        done = False

        # reward logic
        if not self.picked:
            if self.ambulance_location == self.patient_location:
                reward += 1.0
                self.picked = True
            else:
                reward += 0.2 if distance_to_patient < 5 else -0.1
        else:
            if self.ambulance_location == self.hospital_location:
                reward += 1.0
                done = True
            else:
                reward += 0.2 if distance_to_hospital < 5 else -0.1

        # penalty
        if self.time_elapsed > 20:
            reward -= 0.5
            done = True

        return self._get_obs(), reward, done, {}

    def state(self):
        return self._get_obs()

    def _get_obs(self):
        return Observation(
            ambulance_location=self.ambulance_location,
            patient_location=self.patient_location,
            hospital_location=self.hospital_location,
            time_elapsed=self.time_elapsed
        )
# 🚑 Emergency Ambulance Routing Environment

## Overview
This environment simulates real-world ambulance routing:
- Ambulance travels to patient
- Picks up patient
- Delivers to hospital

## Observation Space
- ambulance_location (int)
- patient_location (int)
- hospital_location (int)
- time_elapsed (int)

## Action Space
- move: forward / backward

## Reward Function
- +0.2 for moving closer
- -0.1 for moving away
- +1.0 for reaching patient
- +1.0 for reaching hospital
- -0.5 for exceeding time

## Tasks
1. Easy → Reach patient
2. Medium → Reach patient and move toward hospital
3. Hard → Complete full route efficiently

## Run Locally
```bash
python inference.py
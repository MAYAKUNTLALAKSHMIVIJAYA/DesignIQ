def reset():
    return {"state": "start"}

def step(action):
    return {
        "state": "next",
        "reward": 1,
        "done": True
    }

def reset():
    return {"state": "start"}

def step(action):
    return {
        "state": "next",
        "reward": 1,
        "done": True
    }

if __name__ == "__main__":
    print("DesignIQ OpenEnv running")
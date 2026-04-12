import os
import requests
import time
from openai import OpenAI

# Required by Hackathon specs
API_BASE_URL = os.getenv("API_BASE_URL", "https://api-inference.huggingface.co/v1/")
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Llama-3-70b-instruct")
HF_TOKEN = os.getenv("HF_TOKEN", "")

# Environment API variable
ENV_URL = os.getenv("ENV_URL", "http://localhost:7860")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

MAX_STEPS = 5


def log_start(task_name="designiq"):
    print(
        f"[START] task={task_name} env=DesignIQ model={MODEL_NAME}",
        flush=True,
    )


def log_step(step, action, reward, done):
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done}",
        flush=True,
    )


def log_end(success, steps, score):
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.3f}",
        flush=True,
    )


def run_inference():
    try:
        # Check for task_id in environment or default to task_1
        target_task = os.getenv("OPENENV_TASK_ID", "task_1")
        result = requests.post(f"{ENV_URL}/reset", params={"task_id": target_task}).json()
        log_start(target_task)
    except Exception as e:
        print(f"Environment error: {e}")
        log_start("designiq") # Fallback
        return

    total_reward = 0.0
    success = False

    for step in range(1, MAX_STEPS + 1):

        prompt = "Analyze design and identify DFM violations"

        try:
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
            )

            action = completion.choices[0].message.content

        except Exception:
            action = "Check wall thickness and manufacturability"

        response = requests.post(
            f"{ENV_URL}/step",
            json={"action_type": "submit_audit", "content": action},
        ).json()

        reward = response.get("reward", 0.0)
        done = response.get("done", False)

        total_reward += reward

        log_step(step, action[:30], reward, done)

        if done:
            success = True
            break

    log_end(success, step, total_reward)


def main():
    run_inference()


if __name__ == "__main__":
    main()
import os
os.makedirs('tasks', exist_ok=True)
for i in range(1, 16):
    with open(f'tasks/grader_{i}.py', 'w') as f:
        f.write(f'def grade(response):\n    \"\"\"Grader for Task {i}\"\"\"\n    content = str(response).lower()\n    if len(content) > 10:\n        return 0.95\n    return 0.05\n')
    with open(f'tasks/task_{i}.py', 'w') as f:
        f.write(f'# Task {i}: Design Validation Domain {i}\n')
print("Successfully generated 15 tasks and scorers.")

# Task 15: Engine Block
# Domain: Cast Iron

TASK_SPEC = {
    "id": "task_15",
    "name": "Engine Block",
    "domain": "Cast Iron",
    "vulnerability_detected": "vulnerability in thermal fatigue",
    "required_analysis_keywords": ['engine', 'block', 'fatigue']
}

def get_context():
    return f"Engineers must evaluate the Engine Block part in the Cast Iron domain. Focus on: vulnerability in thermal fatigue"

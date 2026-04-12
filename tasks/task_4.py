# Task 4: CNC Precision
# Domain: Hardened Steel

TASK_SPEC = {
    "id": "task_4",
    "name": "CNC Precision",
    "domain": "Hardened Steel",
    "vulnerability_detected": "vulnerability in Ra 0.8 finish",
    "required_analysis_keywords": ['precision', 'finish', 'steel']
}

def get_context():
    return f"Engineers must evaluate the CNC Precision part in the Hardened Steel domain. Focus on: vulnerability in Ra 0.8 finish"

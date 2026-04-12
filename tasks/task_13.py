# Task 13: Composite Layup
# Domain: Carbon Fiber

TASK_SPEC = {
    "id": "task_13",
    "name": "Composite Layup",
    "domain": "Carbon Fiber",
    "vulnerability_detected": "vulnerability in delamination",
    "required_analysis_keywords": ['composite', 'carbon', 'ply']
}

def get_context():
    return f"Engineers must evaluate the Composite Layup part in the Carbon Fiber domain. Focus on: vulnerability in delamination"

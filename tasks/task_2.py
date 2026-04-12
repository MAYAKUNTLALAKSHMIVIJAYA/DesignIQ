# Task 2: Injection Molding
# Domain: ABS Plastic

TASK_SPEC = {
    "id": "task_2",
    "name": "Injection Molding",
    "domain": "ABS Plastic",
    "vulnerability_detected": "vulnerability in 0.5 deg draft",
    "required_analysis_keywords": ['draft', 'molding', 'abs']
}

def get_context():
    return f"Engineers must evaluate the Injection Molding part in the ABS Plastic domain. Focus on: vulnerability in 0.5 deg draft"

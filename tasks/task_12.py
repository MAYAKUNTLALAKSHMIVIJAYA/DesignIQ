# Task 12: Turbine Blade
# Domain: Superalloy

TASK_SPEC = {
    "id": "task_12",
    "name": "Turbine Blade",
    "domain": "Superalloy",
    "vulnerability_detected": "vulnerability in creep life",
    "required_analysis_keywords": ['turbine', 'blade', 'creep']
}

def get_context():
    return f"Engineers must evaluate the Turbine Blade part in the Superalloy domain. Focus on: vulnerability in creep life"

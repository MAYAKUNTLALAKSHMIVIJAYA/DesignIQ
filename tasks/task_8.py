# Task 8: Die Casting
# Domain: Zinc Alloy

TASK_SPEC = {
    "id": "task_8",
    "name": "Die Casting",
    "domain": "Zinc Alloy",
    "vulnerability_detected": "vulnerability in porosity risk",
    "required_analysis_keywords": ['die', 'casting', 'zinc']
}

def get_context():
    return f"Engineers must evaluate the Die Casting part in the Zinc Alloy domain. Focus on: vulnerability in porosity risk"

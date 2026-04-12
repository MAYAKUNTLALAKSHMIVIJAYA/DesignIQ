# Task 7: Sheet Metal
# Domain: Stainless Steel

TASK_SPEC = {
    "id": "task_7",
    "name": "Sheet Metal",
    "domain": "Stainless Steel",
    "vulnerability_detected": "vulnerability in bend radius",
    "required_analysis_keywords": ['sheet', 'metal', 'bend']
}

def get_context():
    return f"Engineers must evaluate the Sheet Metal part in the Stainless Steel domain. Focus on: vulnerability in bend radius"

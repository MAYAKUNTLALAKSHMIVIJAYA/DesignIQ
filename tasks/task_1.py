# Task 1: Wall Thickness
# Domain: CNC Aluminum

TASK_SPEC = {
    "id": "task_1",
    "name": "Wall Thickness",
    "domain": "CNC Aluminum",
    "vulnerability_detected": "vulnerability in 1.2mm rib",
    "required_analysis_keywords": ['thickness', 'rib', 'aluminum']
}

def get_context():
    return f"Engineers must evaluate the Wall Thickness part in the CNC Aluminum domain. Focus on: vulnerability in 1.2mm rib"

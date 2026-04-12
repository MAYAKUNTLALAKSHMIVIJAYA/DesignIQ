# Task 10: PCB Enclosure
# Domain: Polycarbonate

TASK_SPEC = {
    "id": "task_10",
    "name": "PCB Enclosure",
    "domain": "Polycarbonate",
    "vulnerability_detected": "vulnerability in snap-fit",
    "required_analysis_keywords": ['pcb', 'enclosure', 'snap-fit']
}

def get_context():
    return f"Engineers must evaluate the PCB Enclosure part in the Polycarbonate domain. Focus on: vulnerability in snap-fit"

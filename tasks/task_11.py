# Task 11: Heat Sink
# Domain: Copper

TASK_SPEC = {
    "id": "task_11",
    "name": "Heat Sink",
    "domain": "Copper",
    "vulnerability_detected": "vulnerability in fin spacing",
    "required_analysis_keywords": ['heat', 'sink', 'copper']
}

def get_context():
    return f"Engineers must evaluate the Heat Sink part in the Copper domain. Focus on: vulnerability in fin spacing"

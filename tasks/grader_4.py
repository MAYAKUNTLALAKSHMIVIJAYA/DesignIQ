def grade(response):
    """Grader for Task 4: CNC Precision"""
    content = str(response).lower()
    if "precision" in content and "tolerance" in content:
        return 0.95
    elif "precision" in content:
        return 0.6
    return 0.05

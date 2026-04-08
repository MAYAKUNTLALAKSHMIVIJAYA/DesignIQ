def grade(response):
    """Grader for Task 3: Aerospace"""
    content = str(response).lower()
    if "aerospace" in content and "titanium" in content and ("far" in content or "certification" in content):
        return 1.0
    elif "aerospace" in content and "titanium" in content:
        return 0.7
    return 0.0

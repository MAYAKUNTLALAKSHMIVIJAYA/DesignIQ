def grade(response):
    """Grader for Task 5: Additive Validation"""
    content = str(response).lower()
    if "additive" in content and "support" in content and "orientation" in content:
        return 0.95
    elif "additive" in content and "support" in content:
        return 0.65
    return 0.05

def grade(response):
    """Grader for Task 1: Wall Thickness"""
    content = str(response).lower()
    if "thickness" in content and "critical" in content:
        return 0.95
    elif "thickness" in content:
        return 0.5
    return 0.05

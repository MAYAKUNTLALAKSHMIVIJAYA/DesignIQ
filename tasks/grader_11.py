def grade(response):
    """Grader for Task 11"""
    content = str(response).lower()
    if len(content) > 10:
        return 0.95
    return 0.05

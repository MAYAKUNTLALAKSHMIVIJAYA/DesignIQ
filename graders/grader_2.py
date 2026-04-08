def grade(response):
    """Grader for Task 2: Injection Molding"""
    content = str(response).lower()
    score = 0.0
    if "draft" in content:
        score += 0.5
    if "fillet" in content or "radius" in content:
        score += 0.5
    return score

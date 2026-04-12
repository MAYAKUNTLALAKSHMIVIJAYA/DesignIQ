def grade(response):
    """Grader for Task 2: Injection Molding"""
    content = str(response).lower()
    score = 0.05
    if "draft" in content:
        score += 0.45
    if "fillet" in content or "radius" in content:
        score += 0.45
    return score

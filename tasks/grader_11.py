def grade(response):
    """Advanced Grader for Heat Sink (Copper)"""
    content = str(response).lower()
    score = 0.05
    keywords = ["heat", "sink", "copper"]
    
    # Calculate keyword coverage
    matches = sum(1 for kw in keywords if kw in content)
    
    if matches >= len(keywords) - 1 and len(keywords) > 1:
        score = 0.95
    elif matches >= 1:
        score = 0.5
    
    # Penalize short/unprofessional responses
    if len(content) < 50:
        score = min(score, 0.3)
    
    # Final clamping for validator (0, 1) range
    return max(0.01, min(0.99, score))

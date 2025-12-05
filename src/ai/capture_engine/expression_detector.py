# expression_detector.py - placeholder using mean brightness to 'detect' smile
def detect_expression(frame):
    # placeholder: production code should use fer or a trained model
    # Return one of: neutral, happy, surprise, angry
    import numpy as np
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mean = gray.mean()
    if mean > 120:
        return "happy", 0.9
    return "neutral", 0.8

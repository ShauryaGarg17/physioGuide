import numpy as np

def calculate_angle(a, b, c):
    """
    Calculate the angle between three points
    Args:
        a: First point [x, y]
        b: Mid point [x, y]
        c: End point [x, y]
    Returns:
        angle: Angle in degrees
    """
    if not (len(a) == len(b) == len(c) == 2):
        raise ValueError("Input points must be 2D coordinates.")

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    cosine_angle = np.clip(cosine_angle, -1.0, 1.0)  # Clip to avoid floating point issues
    angle = np.degrees(np.arccos(cosine_angle))

    return angle
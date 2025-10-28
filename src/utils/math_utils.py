"""
Math Utilities - Common mathematical functions
Team Member 4 should expand this
"""

import math
import pygame


def clamp(value, min_val, max_val):
    """Clamp a value between min and max"""
    return max(min_val, min(value, max_val))


def lerp(a, b, t):
    """Linear interpolation between a and b"""
    return a + (b - a) * t


def distance(point1, point2):
    """Calculate distance between two points"""
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def normalize_vector(vector):
    """Normalize a vector to unit length"""
    length = vector.length()
    if length == 0:
        return pygame.Vector2(0, 0)
    return vector / length


def angle_to_vector(angle):
    """Convert angle in radians to unit vector"""
    return pygame.Vector2(math.cos(angle), math.sin(angle))


def vector_to_angle(vector):
    """Convert vector to angle in radians"""
    return math.atan2(vector.y, vector.x)
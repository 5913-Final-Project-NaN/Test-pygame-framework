"""
Transform Component - Position, rotation, scale
Team Member 3 should implement this
"""

import pygame
from .component import Component


class Transform(Component):
    """Component for position, rotation, and scale"""
    
    def __init__(self, x=0, y=0, rotation=0, scale_x=1, scale_y=1):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.rotation = rotation
        self.scale = pygame.Vector2(scale_x, scale_y)
    
    @property
    def x(self):
        return self.position.x
    
    @x.setter
    def x(self, value):
        self.position.x = value
    
    @property
    def y(self):
        return self.position.y
    
    @y.setter
    def y(self, value):
        self.position.y = value
    
    def move(self, dx, dy):
        """Move by delta values"""
        self.position.x += dx
        self.position.y += dy
    
    def set_position(self, x, y):
        """Set absolute position"""
        self.position.x = x
        self.position.y = y
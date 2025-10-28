"""
Game Clock - Manages frame rate and timing
"""

import pygame


class GameClock:
    def __init__(self, fps=60):
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.dt = 0
        
    def tick(self):
        """Tick the clock and return delta time in seconds"""
        self.dt = self.clock.tick(self.fps) / 1000.0
        return self.dt
    
    def get_fps(self):
        """Get current FPS"""
        return self.clock.get_fps()
    
    def get_dt(self):
        """Get delta time"""
        return self.dt
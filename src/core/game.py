"""
Core Game Class - Main game engine implementation
Handles initialization, game loop, and core functionality
"""

import pygame
import sys
from ..utils.asset_loader import AssetLoader
from ..scenes.scene_manager import SceneManager
from ..core.event_manager import EventManager
from ..core.clock import GameClock


class Game:
    def __init__(self, width=1280, height=720, title="Pygame Game"):
        """Initialize the game engine"""
        pygame.init()
        
        # Screen setup
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        
        # Core systems
        self.clock = GameClock()
        self.event_manager = EventManager()
        self.scene_manager = SceneManager()
        self.asset_loader = AssetLoader()
        
        # Game state
        self.running = True
        
    def run(self):
        """Main game loop"""
        while self.running:
            dt = self.clock.tick()
            
            # Handle events
            events = pygame.event.get()
            self.handle_events(events)
            
            # Update current scene
            current_scene = self.scene_manager.get_current_scene()
            if current_scene:
                current_scene.update(dt)
            
            # Render
            self.render()
            
        self.quit()
    
    def handle_events(self, events):
        """Process pygame events"""
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.event_manager.handle_event(event)
                
                # Pass events to current scene
                current_scene = self.scene_manager.get_current_scene()
                if current_scene:
                    current_scene.handle_event(event)
    
    def render(self):
        """Render the current frame"""
        self.screen.fill((0, 0, 0))  # Clear screen
        
        # Render current scene
        current_scene = self.scene_manager.get_current_scene()
        if current_scene:
            current_scene.render(self.screen)
        
        pygame.display.flip()
    
    def quit(self):
        """Clean shutdown"""
        pygame.quit()
        sys.exit()
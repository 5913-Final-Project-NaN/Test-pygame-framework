"""
Main entry point for the Pygame Framework
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.game import Game
from src.scenes.scene_manager import BaseScene
import pygame


class TestScene(BaseScene):
    """Simple test scene to demonstrate the framework"""
    
    def __init__(self):
        super().__init__()
        self.font = None
        
    def enter(self):
        """Initialize the scene"""
        self.font = pygame.font.Font(None, 36)
        
    def update(self, dt):
        """Update scene logic"""
        pass
        
    def render(self, screen):
        """Render the scene"""
        # Clear screen
        screen.fill((50, 50, 100))
        
        # Render text
        if self.font:
            text = self.font.render("Pygame Framework Test", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width()//2, screen.get_height()//2))
            screen.blit(text, text_rect)
            
            info_text = self.font.render("Press ESC to quit", True, (200, 200, 200))
            info_rect = info_text.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 50))
            screen.blit(info_text, info_rect)
    
    def handle_event(self, event):
        """Handle pygame events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def main():
    """Main function"""
    # Create game instance
    game = Game(width=1280, height=720, title="Pygame Framework Test")
    
    # Create and add test scene
    test_scene = TestScene()
    game.scene_manager.add_scene("test", test_scene)
    game.scene_manager.change_scene("test")
    
    # Start the game
    game.run()


if __name__ == "__main__":
    main()
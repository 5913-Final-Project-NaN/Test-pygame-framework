"""
Asset Loader - Manages loading and caching of game assets
"""

import pygame
import os
from typing import Dict, Optional


class AssetLoader:
    def __init__(self):
        self.images: Dict[str, pygame.Surface] = {}
        self.sounds: Dict[str, pygame.mixer.Sound] = {}
        self.fonts: Dict[str, pygame.font.Font] = {}
        
        # Set asset paths
        self.assets_dir = os.path.join(os.path.dirname(__file__), '../../assets')
        self.images_dir = os.path.join(self.assets_dir, 'images')
        self.sounds_dir = os.path.join(self.assets_dir, 'sounds')
        self.fonts_dir = os.path.join(self.assets_dir, 'fonts')
    
    def load_image(self, filename: str, convert_alpha=True) -> Optional[pygame.Surface]:
        """Load and cache an image"""
        if filename in self.images:
            return self.images[filename]
        
        filepath = os.path.join(self.images_dir, filename)
        if os.path.exists(filepath):
            try:
                image = pygame.image.load(filepath)
                if convert_alpha:
                    image = image.convert_alpha()
                else:
                    image = image.convert()
                
                self.images[filename] = image
                return image
            except pygame.error as e:
                print(f"Could not load image {filename}: {e}")
                return None
        else:
            print(f"Image file not found: {filepath}")
            return None
    
    def load_sound(self, filename: str) -> Optional[pygame.mixer.Sound]:
        """Load and cache a sound"""
        if filename in self.sounds:
            return self.sounds[filename]
        
        filepath = os.path.join(self.sounds_dir, filename)
        if os.path.exists(filepath):
            try:
                sound = pygame.mixer.Sound(filepath)
                self.sounds[filename] = sound
                return sound
            except pygame.error as e:
                print(f"Could not load sound {filename}: {e}")
                return None
        else:
            print(f"Sound file not found: {filepath}")
            return None
    
    def load_font(self, filename: str, size: int) -> Optional[pygame.font.Font]:
        """Load and cache a font"""
        key = f"{filename}_{size}"
        if key in self.fonts:
            return self.fonts[key]
        
        if filename is None:
            # Use default font
            font = pygame.font.Font(None, size)
        else:
            filepath = os.path.join(self.fonts_dir, filename)
            if os.path.exists(filepath):
                try:
                    font = pygame.font.Font(filepath, size)
                except pygame.error as e:
                    print(f"Could not load font {filename}: {e}")
                    font = pygame.font.Font(None, size)
            else:
                print(f"Font file not found: {filepath}, using default")
                font = pygame.font.Font(None, size)
        
        self.fonts[key] = font
        return font
    
    def get_image(self, filename: str) -> Optional[pygame.Surface]:
        """Get a cached image"""
        return self.images.get(filename)
    
    def get_sound(self, filename: str) -> Optional[pygame.mixer.Sound]:
        """Get a cached sound"""
        return self.sounds.get(filename)
    
    def get_font(self, filename: str, size: int) -> Optional[pygame.font.Font]:
        """Get a cached font"""
        key = f"{filename}_{size}"
        return self.fonts.get(key)
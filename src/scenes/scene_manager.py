"""
Scene Manager - Handles scene transitions and state management
"""

from typing import Dict, Optional


class BaseScene:
    """Base class for all game scenes"""
    
    def __init__(self):
        self.active = True
    
    def enter(self):
        """Called when entering this scene"""
        pass
    
    def exit(self):
        """Called when exiting this scene"""
        pass
    
    def update(self, dt):
        """Update scene logic"""
        pass
    
    def render(self, screen):
        """Render scene"""
        pass
    
    def handle_event(self, event):
        """Handle pygame events"""
        pass


class SceneManager:
    def __init__(self):
        self.scenes: Dict[str, BaseScene] = {}
        self.current_scene: Optional[str] = None
        self.previous_scene: Optional[str] = None
    
    def add_scene(self, name: str, scene: BaseScene):
        """Add a scene to the manager"""
        self.scenes[name] = scene
    
    def remove_scene(self, name: str):
        """Remove a scene from the manager"""
        if name in self.scenes:
            del self.scenes[name]
    
    def change_scene(self, name: str):
        """Change to a different scene"""
        if name not in self.scenes:
            raise ValueError(f"Scene '{name}' not found")
        
        # Exit current scene
        if self.current_scene:
            current = self.scenes[self.current_scene]
            current.exit()
        
        # Store previous scene
        self.previous_scene = self.current_scene
        self.current_scene = name
        
        # Enter new scene
        new_scene = self.scenes[name]
        new_scene.enter()
    
    def get_current_scene(self) -> Optional[BaseScene]:
        """Get the currently active scene"""
        if self.current_scene:
            return self.scenes[self.current_scene]
        return None
    
    def get_previous_scene(self) -> Optional[BaseScene]:
        """Get the previous scene"""
        if self.previous_scene:
            return self.scenes[self.previous_scene]
        return None
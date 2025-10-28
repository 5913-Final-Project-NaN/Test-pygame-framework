"""
Base Component Class
Team Member 3 should expand this
"""


class Component:
    """Base class for all components in ECS"""
    
    def __init__(self):
        self.entity = None
    
    def update(self, dt):
        """Update component logic"""
        pass
    
    def render(self, screen):
        """Render component"""
        pass
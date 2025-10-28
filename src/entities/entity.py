"""
Entity Component System - Base Entity Class
Team Member 3 should implement this
"""

from typing import Dict, Type, Optional
from ..components.component import Component


class Entity:
    """Base entity class for ECS architecture"""
    
    def __init__(self, entity_id: int):
        self.id = entity_id
        self.components: Dict[Type[Component], Component] = {}
        self.active = True
    
    def add_component(self, component: Component):
        """Add a component to this entity"""
        component_type = type(component)
        self.components[component_type] = component
        component.entity = self
    
    def remove_component(self, component_type: Type[Component]):
        """Remove a component from this entity"""
        if component_type in self.components:
            del self.components[component_type]
    
    def get_component(self, component_type: Type[Component]) -> Optional[Component]:
        """Get a component of specified type"""
        return self.components.get(component_type)
    
    def has_component(self, component_type: Type[Component]) -> bool:
        """Check if entity has a component of specified type"""
        return component_type in self.components
    
    def update(self, dt):
        """Update all components"""
        if self.active:
            for component in self.components.values():
                component.update(dt)
"""
Physics System - Handles physics simulation
Team Member 4 should implement this
"""

import pygame
from typing import List
from ..entities.entity import Entity
from ..components.transform import Transform


class PhysicsSystem:
    """System for handling physics calculations"""
    
    def __init__(self):
        self.gravity = pygame.Vector2(0, 9.81)
        self.entities: List[Entity] = []
    
    def add_entity(self, entity: Entity):
        """Add entity to physics system"""
        if entity not in self.entities:
            self.entities.append(entity)
    
    def remove_entity(self, entity: Entity):
        """Remove entity from physics system"""
        if entity in self.entities:
            self.entities.remove(entity)
    
    def update(self, dt):
        """Update physics for all entities"""
        for entity in self.entities:
            self.update_entity_physics(entity, dt)
    
    def update_entity_physics(self, entity: Entity, dt):
        """Update physics for a single entity"""
        # TODO: Team Member 4 - Implement physics calculations
        # - Apply gravity
        # - Update velocity
        # - Update position based on velocity
        # - Handle collisions
        pass
"""
Event Manager - Handles game events and input
"""

import pygame
from typing import Dict, List, Callable


class EventManager:
    def __init__(self):
        self.listeners: Dict[int, List[Callable]] = {}
        
    def subscribe(self, event_type: int, callback: Callable):
        """Subscribe to an event type"""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)
    
    def unsubscribe(self, event_type: int, callback: Callable):
        """Unsubscribe from an event type"""
        if event_type in self.listeners:
            if callback in self.listeners[event_type]:
                self.listeners[event_type].remove(callback)
    
    def handle_event(self, event):
        """Process an event and notify subscribers"""
        if event.type in self.listeners:
            for callback in self.listeners[event.type]:
                callback(event)
import math

class Arm:
    """
    Represents and arm (or limb) in a kinematic system
    """
    def __init__(self, length, center_angle, rotation_range, phase_offset) -> None:
        self.x = 0
        self.y = 0
        self.length = length
        self.angle = 0
        self.center_angle = center_angle
        self.rotation_range = rotation_range
        self.parent: Arm | None = None
        self.phase_offset = phase_offset
        
    def get_end_x(self):
        """
        Calculates the end x coordinate of an arm
        based on it's starting x, length and angle
        """
        # Add sum of all parent angles to self angle
        angle = self.angle
        parent = self.parent
        while hasattr(parent, "parent"):
            angle += parent.angle
            parent = parent.parent
        
        return self.x + math.cos(angle) * self.length
    
    def get_end_y(self):
        """
        Calculates the end y coordinate of an arm
        based on it's starting y, length and angle
        """
        # Add sum of all parent angles to self angle
        angle = self.angle
        parent = self.parent
        while hasattr(parent, "parent"):
            angle += parent.angle
            parent = parent.parent
        
        # Calculate and return the position
        return self.y + math.sin(angle) * self.length
    
    
    def set_phase(self, phase):
        self.angle = self.center_angle + math.sin(phase + self.phase_offset) * self.rotation_range
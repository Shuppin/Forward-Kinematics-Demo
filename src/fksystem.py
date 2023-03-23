from arm import Arm

# Forward Kinematics System

class ForwardKinematicSystem:
    def __init__(self, x, y):
        self.arms: list[Arm] = []
        self.last_arm = None
        self.origin_x = x
        self.origin_y = y
        self.phase = 0
        self.speed = 0.02
        
    def add_arm(self, length, center_angle, rotation_range, phase_offset):
        """
        Appends an arm onto the system
        """
        arm = Arm(length, center_angle, rotation_range, phase_offset)
        
        if self.last_arm is not None:
            arm.parent = self.last_arm
            
        self.last_arm = arm
        self.arms.append(arm)
            
    def get_arms(self):
        return self.arms
        
    def update(self):
        for arm in self.arms:
            
            arm.set_phase(self.phase)
            
            if arm.parent is not None:
                arm.x = arm.parent.get_end_x()
                arm.y = arm.parent.get_end_y()
            else:
                arm.x = self.origin_x
                arm.y = self.origin_y
                
        self.phase += self.speed
                
    
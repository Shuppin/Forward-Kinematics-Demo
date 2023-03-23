from pyray import *

import math
import numpy as np

from arm        import Arm
from fksystem   import ForwardKinematicSystem
from vec2       import Vec2

# Constants --------------------------------------------------------------------
PADDING = 10
# ------------------------------------------------------------------------------

# Initialisation ---------------------------------------------------------------
init_window(800, 450, "fk_demo_1")
set_target_fps(120)

screen_width, screen_height = get_screen_width(), get_screen_height()

# Create both FK systems which hold all the arms in a kinematic system
# and is resposible for updating each of the arm's positions
fk_system_1 = ForwardKinematicSystem(
    int(screen_width//2), int(screen_height//2)
)
fk_system_2 = ForwardKinematicSystem(
    int(screen_width//2), int(screen_height//2)
)
fk_system_2.phase = math.pi  # Set the phase 1 radian apart, this makes the legs half a cycle apart

# Add arms to the systems
fk_system_1.add_arm(100, math.pi/2, math.pi/4, 0)
fk_system_1.add_arm(90, 0.87, 0.87, -1.5)

fk_system_2.add_arm(100, math.pi/2, math.pi/4, 0)
fk_system_2.add_arm(90, 0.87, 0.87, -1.5)
# ------------------------------------------------------------------------------

def limb_between_points(p1: Vec2, p2: Vec2):
    """
    Draws an ellipse connecting two points
    """
    # Calculate the point between p1 and p2 to set as the center of our ellipse
    midpoint_x = int((p1.x+p2.x) / 2)
    midpoint_y = int((p1.y+p2.y) / 2)
    
    # Calculate the angle between the two points and convert from radians to degrees
    angle = math.atan2(p2.y - p1.y, p2.x - p1.x) * 180 / math.pi
    
    # Set radii of ellipse
    radius_1 = math.sqrt((p2.y-p1.y)**2 + (p2.x-p1.x)**2)//2
    radius_2 = 10  # This value is essetially the 'thickness' of the limb

    rl_push_matrix()                                # Enter a new local space
    rl_translatef(midpoint_x, midpoint_y, 0)        # Move local space origin to midpoint
    rl_rotatef(angle, 0, 0, 1)                      # Rotate local space origin to the angle between p1 and p2
    draw_ellipse(0, 0, radius_1, radius_2, RED)     # Draw the ellipse
    rl_pop_matrix()                                 # Return to world space

while not window_should_close():

    # Update -----------------------------------------------------------------------
    fk_system_1.update()
    fk_system_2.update()
    # ------------------------------------------------------------------------------
    
    # Draw -------------------------------------------------------------------------
    begin_drawing()

    clear_background(BLACK)
    
    # Draw the first 'leg'
    for arm in fk_system_1.get_arms():
        limb_between_points(Vec2.from_(arm), Vec2.from_((arm.get_end_x(), arm.get_end_y())))
    
    # Draw the second 'leg'
    for arm in fk_system_2.get_arms():
        limb_between_points(Vec2.from_(arm), Vec2.from_((arm.get_end_x(), arm.get_end_y())))

    draw_text("fk_demo_1", 0+PADDING, 0+PADDING, 20, VIOLET)

    end_drawing()
    # ------------------------------------------------------------------------------

close_window()
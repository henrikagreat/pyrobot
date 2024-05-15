import pygame
from button_name import ButtonName
from button_action import ButtonAction
from button_event import ButtonEvent

# ========== Playstation controller mapping ==========
# --- Buttons (value is 0 by defualt, 1 when pressed) ---
# Button 0: X
# Button 1: Circle
# Button 2: Square
# Button 3: Triangle
# Button 4: Top left small button
# Button 5: Playstation logo button
# Button 6: Top right small button
# Button 7: Left stick press
# Button 8: Right stick press
# Button 9: L1
# Button 10: R1
# Button 11: D-pad Up
# Button 12: D-pad Down
# Button 13: D-pad Left
# Button 14: D-pad Right
# Button 15: Touchpad press
# Button 16: ?
 
# --- Axes (range from -1 to 1) ---
# Axis 0: Left joystick X-dir (-1 to 1, left to right)
# Axis 1: Left joystick Y-dir (-1 to 1, up to down)
# Axis 2: Right joystick X-dir (-1 to 1, left to right)
# Axis 3: Right joystick Y-dir (-1 to 1, up to down)
# Axis 4: L2 (-1 to 1, fully released to fully pressed)
# Axis 5: R2 (-1 to 1, fully released to fully pressed)

class Controller():

    def __init__(self):
        pygame.init()
        self.joysticks = {}

    def getInput(self):
        event = pygame.event.wait()

        if event.type == pygame.JOYBUTTONDOWN:
            print(f"ButtonDown: {event.button}")
            return ButtonEvent(ButtonAction.BUTTON_DOWN, ButtonName(event.button))

        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            return ButtonEvent(ButtonAction.BUTTON_UP, ButtonName(event.button))
        
        return None

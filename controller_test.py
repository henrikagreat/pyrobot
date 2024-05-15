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
 
ps5_button_map = {
    0: 'X',
    1: 'Circle',
    2: 'Square',
    3: 'Triangle',
    4: 'Top left small button',
    5: 'Playstation logo button',
    6: 'Top right small button',
    7: 'Left stick press',
    8: 'Right stick press',
    9: 'L1',
    10: 'R1',
    11: 'D-pad Up',
    12: 'D-pad Down',
    13: 'D-pad Left',
    14: 'D-pad Right',
    15: 'Touchpad press',
    16: '?'
}
 
ps5_axis_map = {
    0: 'Left joystick X-dir',
    1: 'Left joystick Y-dir',
    2: 'Right joystick X-dir',
    3: 'Right joystick Y-dir',
    4: 'L2',
    5: 'R2'
}
 
 
import pygame
 
from motor import *
 
def main():
    joysticks = {}

    pygame.init()
 
    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.
 
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                if event.button == 0:
                    joystick = joysticks[event.instance_id] 
                    if joystick.rumble(0, 0.7, 500): 
                        print(f"Rumble effect played on joystick {event.instance_id}") 
                if event.button == 3:
                    run(1)
 
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
                if event.button == 3:
                    stop()
 
            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")
                print("We're in.")
 
            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")
                print("We're out.")
 
if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

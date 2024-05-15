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

import pygame
from button_map import ButtonMap
from motor import Motor
from distance import Distance
 
def main():
    pygame.init()

    joysticks = {}
    done = False
    motor = Motor()
    distance = Distance()

    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.
 
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"ButtonDown: {event.button}")

                if event.button == ButtonMap.TRIANGLE:
                    motor.forward()
                    distance.readDistance()
                elif event.button == ButtonMap.SQUARE:
                    motor.turn_left()
                elif event.button == ButtonMap.CIRCLE:
                    motor.turn_right()
                elif event.button == ButtonMap.CROSS:
                    motor.reverse()
 
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
                motor.stop()
 
            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connected")
                print("We're in.")
 
            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")
                print("We're out.")
 
if __name__ == "__main__":
    main()
    pygame.quit()

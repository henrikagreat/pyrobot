from motor import Motor
from distance import Distance
from controller import Controller
from button_action import ButtonAction
from button_name import ButtonName
import random
import time

def main():
    done = False
    motor = Motor()
    controller = Controller()
    distance = Distance()

    while not done:
        try:
            use_distance(distance, motor)
            #use_controller(controller, motor)
        except Exception as e:
            return

def use_distance(distance, motor):
    current_distance = distance.readDistance()

    if current_distance >= 10:
        motor.forward()
    else:
        motor.turn_left()


def use_controller(controller, motor):
    button_event = controller.getInput()

    if button_event == None:
        return

    if button_event.getAction() == ButtonAction.BUTTON_DOWN:
        if button_event.getName() == ButtonName.TRIANGLE:
            motor.forward()
        elif button_event.getName() == ButtonName.SQUARE:
            motor.turn_left()
        elif button_event.getName() == ButtonName.CIRCLE:
            motor.turn_right()
        elif button_event.getName() == ButtonName.CROSS:
            motor.reverse()
    
    if button_event.getAction() == ButtonAction.BUTTON_UP:
        motor.stop()

if __name__ == "__main__":
    main()


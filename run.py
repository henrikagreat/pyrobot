from motor import Motor
from distance import Distance
from controller import Controller
from button_action import ButtonAction
from button_name import ButtonName

def main():
    done = False
    motor = Motor()
    controller = Controller()
    distance = Distance()

    while not done:
        try:
            #current_distance = distance.readDistance()
            use_controller(controller, motor)
        except Exception as e:
            return

def use_controller(controller, motor):
    button_event = controller.getInput()

    print(button_event)

    if button_event == None:
        return

    if button_event.getAction() == ButtonAction.BUTTON_DOWN:
        if button_event.getName() == ButtonName.TRIANGLE:
            motor.forward()

if __name__ == "__main__":
    main()


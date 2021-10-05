
from prac_08.car import Car
from prac_08.unreliable_car import Unreliable

def main():
    """Demo test code to show how to use car class."""

    test_drive = Unreliable("Car",100,)
    print(test_drive)
    test_drive.drive(40)
    print(test_drive)

main()
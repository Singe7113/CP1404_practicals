from prac_08.car import Car
from prac_08.taxi import Taxi


def main():
    """Demo test code to show how to use car class."""
    my_car = Car('car', 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    taxi_ride = Taxi('Prius 1', 100)
    taxi_ride.start_fare()
    taxi_ride.drive(40)
    print(taxi_ride)
    print('cost of trip is $', taxi_ride.get_fare())
    taxi_ride.add_fuel(40)
    taxi_ride.start_fare()
    taxi_ride.drive(100)
    taxi_ride.get_fare()
    print(taxi_ride)
    print('cost of trip is $', taxi_ride.get_fare())


main()

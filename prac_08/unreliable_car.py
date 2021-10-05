from prac_08.car import Car
import random

class Unreliable(Car):
    "speliszed version of car, but like it is unreliable"

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}".format(super().__str__())

    def drive(self, distance):
        engine_ignition = random.uniform(0,1)
        reliability = random.uniform(0, 1)
        if engine_ignition < reliability:
            """Drive like parent Car but calculate fare distance as well."""
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
            return print("ignition"),distance_driven
        else:
            return print("engine failed")

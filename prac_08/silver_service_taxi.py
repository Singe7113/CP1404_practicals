from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):

        return '{} plus flag fall of ${})'.format(super().__str__(),
                                                  self.flag_fall)

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.odometer = distance
        return distance_driven

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flag_fall

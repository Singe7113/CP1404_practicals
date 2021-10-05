from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Demo test code to show how to use car class."""
    silver_taxi_ride = SilverServiceTaxi('Prius 1', 100, 2)
    silver_taxi_ride.drive(18)
    print("cost of silver taxi ride is ${}".format(silver_taxi_ride.get_fare()))
    print(silver_taxi_ride)


main()

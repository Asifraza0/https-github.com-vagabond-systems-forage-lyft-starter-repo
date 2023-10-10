from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass


class SpindlerBatteryTest(unittest.TestCase):

    def test_service_interval_is_three_years(self):
        battery = SpindlerBattery()

        self.assertEqual(battery.service_interval, 3)

class SpindlerBattery:

    def __init__(self):
        self.service_interval = **3**
class SpindlerBatteryTest(unittest.TestCase):

    def test_service_interval_is_three_years(self):
        battery = SpindlerBattery()

        self.assertEqual(battery.service_interval, 3)
class CarFactoryTest(unittest.TestCase):

    def test_service_car_with_carrigan_tires(self):
        car_factory = CarFactory()
        tires = [0.8, 0.7, 0.6, 0.5]

        car = car_factory.create_car(tires)

        self.assertTrue(car.needs_tire_service())

    def test_service_car_with_octoprime_tires(self):
        car_factory = CarFactory()
        tires = [0.9, 0.8, 0.7, 0.6]

        car = car_factory.create_car(tires)

        self.assertTrue(car.needs_tire_service())
class CarFactory:

    def __init__(self):
        self.tire_types = {
            "carrigan": CarriganTire,
            "octoprime": OctoprimeTire
        }

    def create_car(self, tires):
        tire_type = self.tire_types[car.type]
        tires = [tire_type(wear) for wear in tires]

        car = Car(tires)

        return car
class Car:

    def __init__(self, tires):
        self.tires = tires

    def needs_tire_service(self):
        if isinstance(self.tires[0], CarriganTire):
            return any(tire.needs_service() for tire in self.tires)
        elif isinstance(self.tires[0], OctoprimeTire):
            return sum(tire.wear for tire in self.tires) >= 3
        else:
            raise NotImplementedError
class CarriganTire:

    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        return self.wear >= 0.9
class OctoprimeTire:

    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        return False

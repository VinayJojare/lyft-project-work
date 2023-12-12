import unittest
from datetime import datetime, timedelta
from car import Car, OctoprimeTires, CarriganTires
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from engine.Battery.spinder_battery import last_service_date, current_year



class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        Car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        Car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        Car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        Car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        Car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        Car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        Car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        Car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        Car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(Car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        Car = Palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(Car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        Car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(Car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        Car = Palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(Car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        Car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        Car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        Car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        Car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        Car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        Car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        Car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date() 
        current_mileage = 30000
        last_service_mileage = 0

        Car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service())
    
class SpindlerBattery(unittest.TestCase):
    # Add tests in test_battery.py
    def test_spindler_battery_needs_service(self):
        spindler_battery = SpindlerBattery(last_service_date, current_year - 3)
        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        spindler_battery = SpindlerBattery(last_service_date, current_year - 2)
        self.assertFalse(spindler_battery.needs_service())

# Add tests in test_car.py
def test_carrigan_tires_need_service(self):
    carrigan_tires = CarriganTires([0.5, 0.6, 0.7, 0.9])
    self.assertTrue(carrigan_tires.needs_service())

def test_carrigan_tires_do_not_need_service(self):
    carrigan_tires = CarriganTires([0.1, 0.2, 0.3, 0.4])
    self.assertFalse(carrigan_tires.needs_service())

def test_octoprime_tires_need_service(self):
    octoprime_tires = OctoprimeTires([1.0, 0.8, 0.7, 0.5])
    self.assertTrue(octoprime_tires.needs_service())

def test_octoprime_tires_do_not_need_service(self):
    octoprime_tires = OctoprimeTires([0.1, 0.2, 0.3, 0.4])
    self.assertFalse(octoprime_tires.needs_service())
       
  

if __name__ == '__main__':
    unittest.main()


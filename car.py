
from engine_service_criteria import EngineServiceCriteria
from battery_service_criteria import BatteryServiceCriteria
from test_car import CarriganTires, OctoprimeTires

class Car:
    def __init__(self, last_service_date,engine: EngineServiceCriteria, battery: BatteryServiceCriteria):
        self.last_service_date = last_service_date
    
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.service_criteria.needs_service()
    
    def get_service_criteria(self):
        return self.service_criteria.get_service_criteria()
    
    def needs_tire_service(self, tire_wear_array):
        if isinstance(self.tires, CarriganTires):
            return any(wear >= 0.9 for wear in tire_wear_array)
        elif isinstance(self.tires, OctoprimeTires):
            return sum(tire_wear_array) >= 3.0
        else:
            return False

# spindler_battery.py
from battery_service_criteria import BatteryServiceCriteria

class SpindlerBattery(BatteryServiceCriteria):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
    
    

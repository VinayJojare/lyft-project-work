from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from engine_service_criteria import EngineServiceCriteria
from battery_service_criteria import BatteryServiceCriteria
class Rorschach(WilloughbyEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.service_criteria = EngineServiceCriteria(last_service_date)
        self.service_criteria = EngineServiceCriteria(current_mileage)
        self.service_criteria = EngineServiceCriteria(last_service_mileage)
        self.battery_criteria = BatteryServiceCriteria(last_service_date) 

    def needs_service(self):
        return self.service_criteria.needs_service() or self.battery_criteria.needs_service()

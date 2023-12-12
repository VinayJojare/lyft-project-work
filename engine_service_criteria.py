from service_criteria import serviceCriteria

class EngineServiceCriteria(serviceCriteria):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
    
    def needs_service(self):
        return self.service_criteria.needs_service()

    
        


from abc import ABC, abstractmethod

class serviceCriteria (ABC):
    @abstractmethod
    def needs_service(self):
        pass
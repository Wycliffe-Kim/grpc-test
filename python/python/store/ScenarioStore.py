from ..container.ScenarioData import ScenarioData
from .IStore import IStore;

class ScenarioStore(IStore):
    scenarios: dict[int, ScenarioData]
    
    def _init(self):
        self.scenarios = dict()
    
    def get_scenarios(self):
        return self.scenarios
        
    def get_scenario(self, id: int):
        scenario: ScenarioData = self.scenarios.get(id)
        return scenario
      
    def set_scenario(self, scenario: ScenarioData):
        self.scenarios[scenario.id] = scenario
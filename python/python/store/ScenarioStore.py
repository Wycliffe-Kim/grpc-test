from ..container.ScenarioData import ScenarioData
from ..type.ScenarioType import ScenarioType
from .IStore import IStore;

class ScenarioStore(IStore):
    scenarios: dict[ScenarioType, ScenarioData]
    
    def _init(self):
        self.scenarios = dict()
    
    def get_scenarios(self):
        return self.scenarios
        
    def get_scenario(self, type: ScenarioType):
        scenario: ScenarioData = self.scenarios.get(type)
        return scenario
      
    def set_scenario(self, scenario: ScenarioData):
        self.scenarios[scenario.type] = scenario
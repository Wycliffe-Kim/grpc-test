import scenario_pb2
import scenario_pb2_grpc

from ..container.ScenarioData import ScenarioData
from ..store.ScenarioStore import ScenarioStore

class ScenarioService(scenario_pb2_grpc.ScenarioServiceServicer):
    def get_scenario(self, request, context):
        print('----- grpc server scenario service get_scenario -----')
        scenario_id = request.id
        scenario = ScenarioStore().get_scenario(scenario_id)
        return self.__to_grpc_scenario_data(scenario)
    
    def get_scenarios(self, request, context):
        print('----- grpc server scenario service get_scenarios -----')
        scenarios = ScenarioStore().get_scenarios()
        scenario_response = []
        for scenario in scenarios.values():
            scenario_response.append(self.__to_grpc_scenario_data(scenario))
            
        return scenario_pb2.ScenarioResponse(data=scenario_response)
    
    def __to_grpc_scenario_data(self, scenario: ScenarioData):
        return scenario_pb2.ScenarioData(
            id=scenario.id,
            type=str(scenario.type).replace('ScenarioType.', ''))
        
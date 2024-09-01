from abc import ABC, abstractmethod


class ScenarioParams:
    pass


class Scenario(ABC):

    app = None
    scenario_params = None

    def __init__(self, app: "aligator.app.App", scenario_params: ScenarioParams = None):
        self.app = app
        if scenario_params:
            self.scenario_params = scenario_params

    @abstractmethod
    def run_scenario(self):
        pass


def get_scenario(scenario: str, app: "ventilator.app.App", scenario_params: ScenarioParams = None):
    if scenario == "custom":
        from aligator.scenarios.custom import Scenario
        return Scenario(app, scenario_params)
    if scenario == "early_expansion":
        from aligator.scenarios.early_expansion import Scenario
        return Scenario(app, None)
    if scenario == "static":
        from aligator.scenarios.static.scenerio import Scenario
        return Scenario(app, scenario_params)
    else:
        raise Exception("Scenerio not implemented")

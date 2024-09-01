from aligator.scenario import Scenario as ScenarioInterface, ScenarioParams


class Scenario(ScenarioInterface):

    def run_scenario(self):
        self.app.log.info("Running custom scenario")
        self.app.log.info(f"Params: {self.scenario_params}")
        pass

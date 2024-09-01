from aligator.scenario import Scenario as ScenarioInterface, ScenarioParams as ScenarioParamsInterface
from aligator.scenarios.static.models.visits import Visit

from datetime import datetime, timedelta

class DayIterator:
    def __init__(self, start_date: str, end_date: str):
        """
        Initialize the iterator with start and end dates.

        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param end_date: The end date in 'YYYY-MM-DD' format.
        """
        self.current_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_date > self.end_date:
            raise StopIteration

        # Store the current date to return it
        current = self.current_date
        # Increment the current date by one day
        self.current_date += timedelta(days=1)
        return current.date()



class ScenarioParams(ScenarioParamsInterface):
    """
    ScenarioParams is a class that holds the parameters for the scenario
    """

    visits = 5
    """visits is a parameter that holds the number of visits"""


class Scenario(ScenarioInterface):

    def __init__(self, app: "aligator.app.App", scenario_params: ScenarioParams = None):
        self.app = app
        if not scenario_params:
            self.scenario_params = ScenarioParams()
        else:
            self.scenario_params = scenario_params


    def init_db(self):
        self.app.db.Base.metadata.create_all(self.app.db.engine)


#1 - Initialise database + tables


    def run_scenario(self):
        self.init_db()
        #iterate over days to  create visits for each day where we provide start date

        start_date = "2024-01-01"
        end_date = "2024-01-10"
        self.app.log.info("Running custom scenario")
        self.app.log.info(f"Params: {self.scenario_params}")

        for day in DayIterator(start_date, end_date):
            for _ in range(self.scenario_params.visits):
                visit = Visit.create_it(dt=day)
                self.app.db.add(visit)

            self.app.db.commit()

        pass

    def get_visits(self):
        return self.scenario_params.visits
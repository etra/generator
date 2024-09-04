from aligator.scenario import Scenario as ScenarioInterface, ScenarioParams as ScenarioParamsInterface
from aligator.scenarios.static.models.visits import Visit, UserType, Search, Order
from datetime import datetime, timedelta
import numpy as np

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

    seed = None
    """seed is a parameter that holds the seed for the random number generator"""

    min_visits = 5
    """min number of visits is a parameter that holds the number of visits"""

    visit_factor = 10
    """multiplication of visit to have total"""


    user_type_predictions = {
        UserType.NEW_USER: 0.3,
        UserType.RETURNING_USER: 0.1,
        UserType.REGISTERED_USER: 0.6
    }
    """user_type_predictions is a parameter that holds the predictions for the user types"""

    search_predictions = {
        UserType.NEW_USER: 0.4,
        UserType.RETURNING_USER: 0.6,
        UserType.REGISTERED_USER: 0.9
    }
    """search_predictions is a parameter that holds the predictions for the search types"""

    order_predictions = {
        UserType.NEW_USER: 0.1,
        UserType.RETURNING_USER: 0.6,
        UserType.REGISTERED_USER: 0.8
    }
    """order_predictions is a parameter that holds the predictions for the order types"""

    registration_predictions = {
        UserType.NEW_USER: 0.5,
        UserType.RETURNING_USER: 0.8,
        UserType.REGISTERED_USER: 0.0
    }
    """registration_predictions is a parameter that holds the predictions for the registration"""

class Scenario(ScenarioInterface):

    def __init__(self, app: "aligator.app.App", scenario_params: ScenarioParams = None):
        self.app = app
        if not scenario_params:
            self.scenario_params = ScenarioParams()
        else:
            self.scenario_params = scenario_params
    def init_db(self):
        self.app.db.Base.metadata.create_all(self.app.db.engine)


    @property
    def seed(self):
        return self.scenario_params.seed if self.scenario_params.seed else np.random.randint(10000000)


#1 - Initialise database + tables
    def run_scenario(self):
        self.init_db()

        #iterate over days to  create visits for each day where we provide start date

        start_date = "2024-01-01"
        end_date = "2024-04-01"
        self.app.log.info("Running custom scenario")
        self.app.log.info(f"Params: {self.scenario_params}")

        for day in DayIterator(start_date, end_date):
            self.generate_day(dt=day)
            # for _ in range(self.scenario_params.visits):
            #     visit = Visit.create_it(dt=day)
            #     self.app.db.add(visit)

            self.app.db.commit()
            #todo: add user creted
            #toto: add order created (for this to work - we need to have products in place)
            #


        pass


    def generate_day(self, dt):
        for _ in range(
                max(
                    np.random.randint(self.scenario_params.visit_factor * self.scenario_params.min_visits),
                    self.scenario_params.min_visits)
        ):
            self.generate_visit(dt)
            self.app.db.commit()
        pass

    def generate_visit(self, dt):
        user_type = np.random.choice(
            list(self.scenario_params.user_type_predictions.keys()),
            p=list(self.scenario_params.user_type_predictions.values())
        )

        visit = Visit.create_it(dt=dt, user_type=user_type)
        self.app.db.add(visit)

        if self.scenario_params.search_predictions[user_type] > np.random.rand():
            self.generate_search(dt=dt, visit=visit)
        else:
            self.app.log.info(f'No search for {visit.user_type}')

    def generate_search(self, dt, visit):
        search = Search.create_it(dt=dt, visit_id=visit.id)
        self.app.db.add(search)
        self.app.log.info(f'Generating search + {visit.user_type}')
        if self.scenario_params.order_predictions[visit.user_type] > np.random.rand():
            self.generate_order(dt, visit, search)
        else:
            self.app.log.info(f'No order for {visit.user_type}')

    def generate_order(self, dt, visit, search):
        order = Order.create_it(dt=dt, search_id=search.id)
        self.app.db.add(order)
        self.app.log.info(f'Generating order + {visit.user_type}')

"""
visit -> search -> order 
100 -> 60% -> 1%

"""

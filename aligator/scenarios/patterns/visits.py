import numpy as np

class Visits:

    def get_visit(self, app):
        return 5
    def radom_visits(self, app, min, max):
        np.random.seed(0)
        return np.random.random_integers(min, max)


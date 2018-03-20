import time

from acoAlgorithm.Simulation import Simulation
from examples.Scenario3 import Scenario3

start = time.clock()
class App:
    def iteration_finished(self,a,b):
        pass

print(time.clock() - start)


app = App()
sim = Simulation(Scenario3)
sim.start(app)
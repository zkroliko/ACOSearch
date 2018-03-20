import sys
import time

from acoAlgorithm.PheromoneMap import PheromoneMap
from acoAlgorithm.Walker import Walker
from acoAlgorithm.tools.Printer import Printer
from examples.Scenario1 import Scenario1

class Simulation:

    DEFAULT_SCENARIO = Scenario1
    DEFAULT_N_ITERATIONS = 400

    DEFAULT_RESULTS_FILE = "iteration_results.csv"
    DEFAULT_OPTIMIZED_FILE = "best_path.csv"


    # Algorithm specific

    def __init__(self):
        self.scenario = self.DEFAULT_SCENARIO
        self.n_iterations = self.DEFAULT_N_ITERATIONS
        self.iteration = 0
        self.result_file = self.DEFAULT_RESULTS_FILE
        self.path_file = self.DEFAULT_OPTIMIZED_FILE
        self.pheromone_map = PheromoneMap()
        self.sh = self.SolutionHolder()

    def get_fields(self):
        printer = Printer(self.scenario.area())
        printer.set_start(self.scenario.start())
        return printer.fields

    def start(self, app):
        # For saving results
        with open(self.result_file, 'w') as result_file:
            for iteration in range(self.n_iterations):
                start = time.time()
                w = Walker(self.scenario.area(), self.scenario.start(), self.pheromone_map)
                while not w.finished():
                    w.step()
                self.pheromone_map.set_update_weight(10000.0 / pow(w.path.__len__(), 2))
                self.pheromone_map.apply_update()
                # Recording data
                self.sh.propose_solution(w)
                data = "%s, %s" % (w.path.__len__(), time.time() - start)
                result_file.write(data + "\n")
                print(data)
                app.iteration_finished(iteration, w.path.__len__())


            printer = Printer(self.scenario.area())
            printer.set_start(self.scenario.start())

            app.result(self)
            print("# Best solution's length is %s" % self.sh.length)
            print("# Best solution is %s" % self.sh.path_to_str())
            print("Iteration progress saved in {}".format(self.result_file))

            with open(self.path_file, 'w') as path_file:
                path_file.write(self.sh.path_to_csv())
                print("Best solution saved in {}".format(self.path_file))


    def best_solution(self):
        return self.sh.path

    class SolutionHolder:
        def __init__(self):
            self.path = None
            self.length = sys.maxsize

        def propose_solution(self, walker):
            if walker.path.__len__() < self.length:
                self.path = walker.path
                self.length = self.path.__len__()

        def path_to_str(self):
            str = ""
            for field in self.path:
                str += field.__str__()
                str += ", "
            return str

        def path_to_csv(self):
            str = ""
            for field in self.path:
                str += "{},{}".format(field.x,field.y)
                str += "\n"
            return str


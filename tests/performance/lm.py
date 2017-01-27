import time

from acoAlgorithm.Point import Point
from acoAlgorithm.View import ViewGenerator
from examples.Scenario1 import Scenario1
from examples.Scenario3 import Scenario3
from examples.Scenario4 import Scenario4

a = Scenario3.area()

v = ViewGenerator(a)
for i in range(a.main.start.x, a.main.end.x):
    for j in range(a.main.start.y, a.main.end.y):
        v.shine_from(Point(i, j))

start = time.clock()

for k in range(10):
    for i in range(a.main.start.x, a.main.end.x):
        for j in range(a.main.start.y, a.main.end.y):
            v.lm.remains_to_be_checked((i, j))

end = time.clock() - start

print "Full: %s" % end

start = time.clock()

for l in range(10):
    v = ViewGenerator(a)
    for i in range(a.main.start.x, a.main.end.x):
        for j in range(a.main.start.y, a.main.end.y):
            v.lm.remains_to_be_checked((i, j))

end = time.clock() - start

end = time.clock() - start

print "Empty: %s" % end
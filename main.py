from calendar import c
from queue import PriorityQueue

queues = [PriorityQueue(), PriorityQueue()]

queues[0].put(1)
queues[0].put(2)
queues[1].put(1)
queues[1].put(2)

if queues[0].get() == 0 and queues[1].get() == 0:
    print(1)
else:
    print(queues[1].qsize())
    print(queues[0].qsize())

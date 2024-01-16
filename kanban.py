import logging
import queue
import threading
import time
from worker import Worker

class Kanban:
    def __init__(self):
        self.staff = Worker(1)
        self.senior1 = Worker(1.25)
        self.senior2 = Worker(1.25)
        self.mid = Worker(1.5)
        self.junior = Worker(2)
        self.worker_pool = [self.staff, self.senior1, self.senior2, self.mid, self.junior]

    def run(self, givenWork):
        logging.debug("python Kanban run method")
        q = queue.Queue()
        q.queue = queue.deque(givenWork)
        startTime = time.time()
        for i in range(len(self.worker_pool)):
            t = threading.Thread(target=self.worker_pool[i].run, args=(givenWork[i], q))
            t.start()
        q.join()
        t.join()
        endTime = time.time()
        logging.debug("python Kanban run method done")
        print("python Kanban run method took " + str(endTime - startTime) + " seconds")
        return

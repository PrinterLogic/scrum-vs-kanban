import logging
import queue
import threading
import time
from worker import Worker

class Scrum:
    def __init__(self, sprint_size):
        self.staff = Worker(1) # 8 points
        self.senior1 = Worker(1.25) # 7 points
        self.senior2 = Worker(1.25) # 7 points
        self.mid = Worker(1.5) # 6 points
        self.junior = Worker(2) # 4 points
        self.worker_pool = [self.staff, self.senior1, self.senior2, self.mid, self.junior]
        self.max_sprint_size = sprint_size

    def run(self, givenWork):
        logging.debug("python Scrum run method")
        q = queue.Queue()
        q.queue = queue.deque(givenWork)

        # build sprint queues
        startTime = time.time()
        while q.qsize() > 0:
            current_sprint_size = 0
            sprint = queue.Queue()
            while current_sprint_size < self.max_sprint_size:
                try:
                    work = q.get(block=False)
                    sprint.put(work, block=False)
                    current_sprint_size += float(work)
                except queue.Empty:
                    break
            # run
            self.runSprint(sprint)

        # make sure the queue is empty
        q.join()
        endTime = time.time()

        logging.debug("python Scrum run method took " + str(endTime - startTime) + " seconds")
        print("python Scrum run method took " + str(endTime - startTime) + " seconds")
        return

    def runSprint(self, sprint: queue.Queue):
        # create threads and run
        threads = []
        for i in range(len(self.worker_pool)):
            t = threading.Thread(target=self.worker_pool[i].run, args=(sprint,))
            threads.append(t)
            t.start()
        # wait for all threads to finish
        for t in threads:
            t.join()
        return
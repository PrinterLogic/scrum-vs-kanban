import time
import logging
import queue

class Worker:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def run(self, work, q: queue.Queue):
        while True:
            work = 0
            try:
                work = q.get(block=False)
            except queue.Empty:
                break
            time.sleep(float(work) * self.multiplier)
        logging.debug("python Worker run method done")
        return
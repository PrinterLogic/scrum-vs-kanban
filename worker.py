import time
import logging
import queue

class Worker:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def run(self, q: queue.Queue):
        while True:
            work = 0
            try:
                work = q.get(block=False)
                time.sleep(float(work) * self.multiplier)
            except queue.Empty:
                break
        logging.debug("python Worker run method done")
        return

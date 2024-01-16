import time
import logging

class Worker:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def run(self, givenWork):
        logging.debug("python Worker run method")
        time.sleep(givenWork * self.multiplier)
        logging.debug("python Worker run method done")
        logging.debug(givenWork * self.multiplier)
import logging
from worker import Worker

class Scrum:
    def __init__(self):
        self.staff = Worker(1)
        self.senior1 = Worker(1.25)
        self.senior2 = Worker(1.25)
        self.mid = Worker(1.5)
        self.junior = Worker(2)

    def run(self, givenWork):
        logging.debug("python Scrum run method")
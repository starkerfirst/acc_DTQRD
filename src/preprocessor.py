import numpy as np
import simpy 
from queue import Queue

class Preprocessor():
    def __init__(self, chip, env) -> None:
        self.queue = Queue(0)
        self.env = env
        self.chip = chip
        self.chip.bram.queue = self.queue # connect with bram

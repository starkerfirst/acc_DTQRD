import numpy as np
import simpy 
from bram import *
from PEarray import *
from collector import *
from preprocessor import *

class Chip():
    def __init__(self, env, N, M) -> None:
        self.N = N
        self.M = M
        self.env = env

        self.bram = Bram(env, self, 0.5, 0.5)
        self.Qcollector = Collector(env, "Q")
        self.Rcollector = Collector(env, "R")
        self.preprocessor = Preprocessor(self, env)
        self.array = Array(env)

        # controller
        self.k = 0

    def controller(self):
        pass


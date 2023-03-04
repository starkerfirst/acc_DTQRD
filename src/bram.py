import numpy as np
import simpy 

class Bram():
    def __init__(self, env, chip, unitReadTime, unitWriteTime) -> None:
        self.mem = []
        self.env = env
        self.queue = None
        self.chip = chip
        self.Qcollector = self.chip.Qcollector
        self.Rcollector = self.chip.Rcollector
        self.rHandle = env.process(self.read(env))
        self.wHandle = env.process(self.write(env))
        self.unitReadTime = unitReadTime
        self.unitWriteTime = unitWriteTime

        self.Index = -1

    def load(self, A):
        self.mem.append(A)

    def access(self, i, isRead):
        return self.mem[i]

    def read(self, env):
        while True:
            if not self.Index==-1:
                j = 0
                while j < len(self.mem[self.Index]):
                    self.queue.put(self.mem[self.Index][j])
                    yield env.timeout(self.unitReadTime)
            else:
                yield env.timeout(1)

    def write(self, env):
        while True:
            if not self.Index == -1:
                j = 0
                while j < len(self.mem[self.Index]):
                    self.queue.put(self.mem[self.Index][j])
                    yield env.timeout(self.unitWriteTime)
                self.Index = -1
            else:
                yield env.timeout(1)

import random

class WeightedRoundRobin:
    def __init__(self, weights):
        self.servers = []
        for i, w in enumerate(weights):
            self.servers.extend([i] * w)

    def select(self):
        return random.choice(self.servers)


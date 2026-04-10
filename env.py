import numpy as np

class NetworkEnv:
    def __init__(self, num_servers=3, capacity=100):
        self.num_servers = num_servers
        self.capacity = capacity
        self.reset()

    def reset(self):
        self.loads = np.zeros(self.num_servers)
        return self.loads

    def step(self, action, traffic):
        self.loads[action] += traffic

        # Reward: balance load
        imbalance = np.std(self.loads)
        reward = -imbalance

        done = False
        return self.loads, reward, done
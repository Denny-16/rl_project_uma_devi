from env import NetworkEnv
from rr import RoundRobin
import numpy as np

env = NetworkEnv()
rr = RoundRobin(3)

state = env.reset()

for _ in range(100):
    action = rr.select()
    traffic = np.random.randint(5, 20)
    state, reward, _ = env.step(action, traffic)

print("Final Loads (RR):", state)


print("Total Traffic:", sum(state))
print("Imbalance (std):", np.std(state))
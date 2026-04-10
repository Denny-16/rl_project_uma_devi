from env import NetworkEnv
from rr import RoundRobin
from wrr import WeightedRoundRobin
from metrics import calculate_metrics
import numpy as np

def run_rr():
    env = NetworkEnv()
    rr = RoundRobin(3)
    state = env.reset()

    for _ in range(100):
        action = rr.select()
        state, _, _ = env.step(action, np.random.randint(5, 20))

    return calculate_metrics(state)

def run_wrr():
    env = NetworkEnv()
    wrr = WeightedRoundRobin([1,2,3])
    state = env.reset()

    for _ in range(100):
        action = wrr.select()
        state, _, _ = env.step(action, np.random.randint(5, 20))

    return calculate_metrics(state)

print("RR:", run_rr())
print("WRR:", run_wrr())
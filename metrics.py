import numpy as np

def calculate_metrics(loads):
    throughput = np.sum(loads)
    imbalance = np.std(loads)
    return throughput, imbalance
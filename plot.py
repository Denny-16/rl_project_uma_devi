import matplotlib.pyplot as plt

methods = ['RR', 'WRR', 'MADQN']
throughput = [1000, 1200, 1500]
imbalance = [30, 20, 10]

plt.figure()
plt.bar(methods, throughput)
plt.title("Throughput Comparison")
plt.show()

plt.figure()
plt.bar(methods, imbalance)
plt.title("Load Imbalance")
plt.show()
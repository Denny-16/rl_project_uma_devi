import torch
import torch.optim as optim
import numpy as np
from env import NetworkEnv
from dqn import DQN

env = NetworkEnv()
model = DQN(3, 3)
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.MSELoss()

gamma = 0.9
epsilon = 0.1

for episode in range(200):
    state = env.reset()

    for _ in range(100):
        state_tensor = torch.FloatTensor(state)

        if np.random.rand() < epsilon:
            action = np.random.randint(0, 3)
        else:
            q_values = model(state_tensor)
            action = torch.argmax(q_values).item()

        traffic = np.random.randint(5, 20)
        next_state, reward, _ = env.step(action, traffic)

        target = reward + gamma * torch.max(model(torch.FloatTensor(next_state))).item()

        target_f = model(state_tensor).clone().detach()
        target_f[action] = target

        loss = loss_fn(model(state_tensor), target_f)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        state = next_state

print("Training Done")
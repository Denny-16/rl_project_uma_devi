class RoundRobin:
    def __init__(self, num_servers):
        self.index = 0
        self.num_servers = num_servers

    def select(self):
        server = self.index
        self.index = (self.index + 1) % self.num_servers
        return server
class TraficLight():
    def __init__(self):
        step = 0
        values = ['RED', 'YELLOW', 'GREEN']
    def print(self):
        print("Svetofor is shining", self.value)
    def step(self):
        if self.step == 2:
            self.step = 0
        else:
            step += 1
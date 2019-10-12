class TraficLight():
    def __init__(self):
        step = 0
        values = ['RED', 'YELLOW', 'GREEN']
    def print(self):
        print('---\n-', "#" if step == 0 else " ", "-\n---\n---\n---\n-",
            "#" if step == 1 else " ", '-\n---\n---\n---\n-',
            "#" if step == 2 else " ", '-\n--', sep='')
    def step(self):
        if self.step == 2:
            self.step = 0
        else:
            step += 1
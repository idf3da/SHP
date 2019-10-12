class TraficLight():
    def __init__(self):
        self.step = 0
        self.values = ['RED', 'YELLOW', 'GREEN']
    def print(self):
        print('---\n-', "#" if self.step == 0 else " ", "-\n---\n---\n---\n-",
            "#" if self.step == 1 else " ", '-\n---\n---\n---\n-',
            "#" if self.step == 2 else " ", '-\n---', sep='')
    def stepChange(self):
        if self.step == 2:
            self.step = 0
        else:
            self.step += 1

a = TraficLight()
a.print()
a.stepChange()
a.print()
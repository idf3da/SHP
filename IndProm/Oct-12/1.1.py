class TraficLight():
    def __init__(self):
        self.step = 2
        self.values = ['RED', 'YELLOW', 'GREEN']
        self.value = self.values[self.step]
    def print(self):
        if self.value != "BLUE":
            print('###\n###')
            print('#', '@#' if self.value == "RED" else " #", sep='')
            print('###')
            print('#', '@#' if self.value == "YELLOW" else " #", sep='')
            print('###')
            print('#', '@#' if self.value == "GREEN" else " #", sep='')
            print('###\n###')
        else:
            print("#-#\n" * 9)
    def stepChange(self):
        if self.value == "GREEN":
            self.value = "YELLOW"
            self.step += 1
        elif self.value == "YELLOW":
            if self.step % 2 == 0:
                self.value = "BLUE"
                self.BLUE_COUNTER = 0
            else:
                self.value = "RED"
            self.step += 1
        elif self.value == "BLUE":
            if self.BLUE_COUNTER < 2:
                self.BLUE_COUNTER += 1
            else:
                self.value = "GREEN"
                self.step += 1
        elif self.value == "RED":
            self.value = "GREEN"
            self.step += 1





a = TraficLight()

while True:
    s = input()
    if s == "P":
        a.print()
    elif s == "S":
        a.stepChange()
from abc import ABC, abstractmethod
class CalcHistory:
    commands = []
    def pop(self):
        return self.commands.pop()

    def push(self,command):
        return self.commands.append(command)


class Command(ABC):
    arr = None 
    @abstractmethod
    def do(self):
        pass
    @abstractmethod
    def undo(self):
        pass
    @abstractmethod
    def __str__(self):
        pass


class ComandExecutor:
    def __init__(self,arr = []):
        self.arr = arr
    history = CalcHistory()
    tmp_ = None

    def do(self,command):
        self.arr = command.do(self.arr)
        self.history.push(command)

    def undo(self,command):
        if len(self.history.commands) > 0: 
            self.arr = command.undo(self.arr)
            self.tmp_ = self.history.pop()
        else:
            print('История пуста')

    def redo(self,command):
        if self.tmp_ is not None:
            self.arr = command.do(self.arr)
            self.history.push(self.tmp_)
            self.tmp_ = None
        else:
            print('Нечего вернуть')

    def __str__(self):
        str_ = ''
        for i in self.arr:
            str_+=str(i)+'\n'
        return str(self.history.commands) +'\n' + str_
        
class Multiply(Command):
    def __init__(self,value):
        #self.arr = arr
        self.value = value

    def do(self,arr):
        return [[j*self.value for j in i] for i in arr]

    def undo(self,arr):
        return [[j/self.value for j in i] for i in arr]

    def __str__(self):
        str_ = ''
        str_+='Провели действие с {0}'.format(self.value)+'\n'
        #for i in self.arr:
        #    str_+=str(i)+'\n'
        return str_

class Power(Command):
    def __init__(self,value):
        #self.arr = arr
        self.value = value

    def do(self,arr):
        return [[j**self.value for j in i] for i in arr]

    def undo(self,arr):
        return [[pow(j, 1/self.value) for j in i] for i in arr]

    def __str__(self):
        str_ = ''
        str_+='Провели действие с {0}'.format(self.value)+'\n'
        #for i in self.arr:
        #    str_+=str(i)+'\n'
        return str_


class App:
    def main(self):
        arr = [[1,2,3],[4]]
        executor = ComandExecutor(arr)

        mult = Multiply(5)
        pow_ = Power(2)


        executor.do(mult)
        print(executor,mult)
        executor.undo(mult)
        print(executor,mult)
        executor.redo(mult)
        print(executor,mult)

        executor.do(pow_)
        print(executor,pow_)
        executor.do(pow_)
        print(executor,pow_)
        executor.undo(pow_)
        print(executor,pow_)
        executor.undo(pow_)
        print(executor,pow_)
        executor.undo(pow_)
        print(executor,pow_)
        executor.redo(pow_)
        print(executor,pow_)

        executor.do(mult)
        print(executor,mult)

        executor.redo(pow_)
        print(executor,pow_)
        executor.undo(pow_)
        print(executor,pow_)
        

app = App()
app.main()



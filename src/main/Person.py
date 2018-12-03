from abc import abstractmethod
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def doSomething(self,action):
        print(self.name + ',' + str(self.age) + '岁'+ ','+action)

class anaim:
    @abstractmethod
    def doSomething(self):
        pass

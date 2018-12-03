class program(object):
    def __init__(self, name, age, weight):
        self.name = name
        self.__weight = weight
        if isinstance(age, int):
            self._age = age
        else:
            raise Exception('age must be a int')

    def __str__(self):
        return self.name + str(self._age) + str(self.__weight)
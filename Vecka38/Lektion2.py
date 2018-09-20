class Person:
    __name = None  # __ = private
    __yrke = None  # annars GLOBAL
    __country = None

    def __init__(self, name, yrke, country):
        self.__name = name
        self.__yrke = yrke
        self.__country = country

    def set_newname(self, name):
        self.__name = name

    def set_yrke(self, yrke):
        self.__yrke = yrke

    def set_country(self, country):
        self.__country = country

    def get_name(self):
        return self.__name

    def get_yrke(self):
        return self.__yrke

    def get_country(self):
        return self.__country


person1 = Person(input('Ange name: '), input('Ange yrke: '), input('Ange land: '))

print('{0} is the coolest cat in town\nYour write your name: {0}\nAnd your age is: {1}\nAnd you living in: {2}'.format(
    person1.get_name(), person1.get_yrke(), person1.get_country()))

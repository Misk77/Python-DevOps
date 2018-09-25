import random
def addTwo(a, b):
    added = a + b
    return added

def Tarning(object):
    def __init__(self,sidor=6):
        self.sidor = sidor
        self.kasta()
        self.__visar = 0

    def kasta(self):
        self.__visar = random.randrange(self.sidor)+1

    def las(self):
        return self.__visar
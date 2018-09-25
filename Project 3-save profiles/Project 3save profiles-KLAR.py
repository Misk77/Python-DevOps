class Profile:
    __name = None  # __ = private
    __yrke = None  # annars GLOBAL
    __age = None
    __country = None

    def __init__(self, name, age, yrke, country):
        self.__name = name
        self.__yrke = yrke
        self.__country = country
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_yrke(self, yrke):
        self.__yrke = yrke

    def set_country(self, country):
        self.__country = country

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_yrke(self):
        return self.__yrke

    def get_country(self):
        return self.__country

    def get_age(self):
        return self.__age


class PersonalInfo(Profile):
    __hobbies = None
    __sex = None
    __length = None

    def __init__(self, name, age, yrke, country, hobbies, sex, length, ):
        self.__hobbies = hobbies
        self.__sex = sex
        self.__length = length
        super().__init__(name, age, yrke, country)

    def set_hobbies(self, hobbies):
        self.set__hobbies = hobbies

    def get_hobbies(self):
        return self.__hobbies

    def set_sex(self, sex):
        self.set__sex = sex

    def get_sex(self):
        return self.__sex

    def set_lenght(self, length):
        self.__length = length

    def get_length(self):
        return self.__length


while True:
    try:
        userList = []
        personinfo = (input('Ange Name: \n'), int(input('Ange Ålder: \n')), input('Ange Yrke: \n'),
                      input('Ange Land: \n'),
                      input('Ange Hobby: \n'),
                      input('Ange sex: \n'), int(input('Ange längd: \n')))
        userList.append(personinfo)
        with open('userList.txt', 'a+') as f:
            for item in userList:
                f.write('\n{0}'.format(userList))
        personinfo = input('\nVill du gå vidare: press enter \nFor exit press {n/N] to exit\n')
        if personinfo == 'n' or 'N':
            break
    except ValueError as e:
        print('Badness {0}', format(e))
svar = input('Inmatningen har avslutas:\n vill du söker efter profil kriterier:(j/n)')
if svar == 'j':
    try:
        fname = input('Ange filnamnet du söker:\n eller vill du öppna userList[ press: 1? ')
        if fname == '1':
            with open('userList.txt', 'r+') as h:
                inp = input('Ange fras du söker: ')
            count = 0
            with open('userList.txt', 'r+') as f:
                for line in f:
                    line = line.rstrip()
                    if line.find(inp) == -1: continue
                    count = count + 1
            print('there were {0} of your search in line'.format(count, ))
            print('-----------------')

    except ValueError as e:
        print('Badness: {0}'.format(e))

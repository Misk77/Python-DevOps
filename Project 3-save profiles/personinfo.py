# coding=utf8
def inputuser():
    userList = []
    personinfo = (input('Ange Name: '), int(input('Ange Ålder')), input('Ange Yrke: '),
                  input('Ange Land: '),
                  input('Ange Hobby: '),
                  input('Ange sex: '), int(input('Ange längd: ')))

    return personinfo
    userList=inputuser()
    userList.append(personinfo)


    i = 0
    while i < len(userList):
        print(userList)
        i += 1

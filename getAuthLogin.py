def getAuthentification():

    with open('secret', 'r', encoding='utf8') as input_file:

        login, pwd = input_file.readline().strip().split(' ')

    return login, pwd

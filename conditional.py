class AuthError(Exception):
    # def __init__(self, expression, message):
        # self.expression = expression
        # self.message = message
    # print('User-defined exception: Auth Error A!')
    def __str__(self):
        return('User-defined exception: Auth Error! B')

def first(password):
    if password == 'password':
        print('step 1')
        return True
    else:
        raise AuthError(password, 'senha errada')

def second(element):
    if element == 'qwerty':
        print('step 2')
        return True


def third(command):
    if type(command) == str:
        print('step 3')
        return True


def main():
    try:
        first('passworda')
        second('qwerty')
        third('ls')
    except Exception as e:
        print('Exceção capturada: ' + str(e))


if __name__ == '__main__':
    main()

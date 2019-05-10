
user_access_table = {
    'apple':    'red',
    'lettuce':  'green',
    'lemon':    'yellow',
    'orange':   'orange',
}


def check_user_access(user_name, password):
    """
    Gets username and password, and check them at user_access_table.
    If OK prints 'Welcome Master' and return True, otherwise prints
    'INTRUDER ALERT' and return False.
    :param user_name: user name string.
    :param password: the password string matching the given username.
    :return: True on exact mach, False otherwise.
    """
    try:
        if user_access_table[user_name] == password:
            print('Welcome Master')
            return True
    except KeyError:
        pass

    print('INTRUDER ALERT')
    return False


while True:
    user_name = input('Username: ')
    password = input('Password: ')
    check_user_access(user_name, password)

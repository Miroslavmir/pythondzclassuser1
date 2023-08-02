

class User:
    def __init__(self, name, surname, login, password):
        self.__name = name
        self.__surname = surname
        self.__login = login # не менее 5 символов
        self.__password = password # не менее 8 символов и должен содержать минимум 3 буквы
    #
    def get_public_user_name(self):
        self.get_private_user_name()
    #
    def get_public_user_surname(self):
        self.get_private_user_surname()
    #
    def get_public_user_login(self):
        if len(self.__login) >= 5:
            print(self.__login)
        else:
            print('error')

    def get_public_user_password(self):
        if len(self.__password) >= 8:
            print(self.__password)
        else:
            print('error')
    #
    # def get_protected_user_name(self):
    #      print(self.__name)
    #
    # def get_protected_user_surname(self):
    #     print(self.__surname)
    #
    # def get_protected_user_login(self):
    #     if len(self.__login) >= 5:
    #         print(self.__login)
    #     else:
    #         print('error')
    #
    # def get_protected_user_password(self):
    #     if len(self.__password) >= 8:
    #         print(self.__password)
    #     else:
    #         print('error')

    def get_private_user_name(self):
        print(self.__name)
    def get_private_user_surname(self):
        print(self.__surname)
    def get_private_user_login(self):
        if len(self.__login) >= 5:
            print(self.__login)
        else:
            print('error')
    def get_private_user_password(self):
        if len(self.__password) >= 8:
            print(self.__password)
        else:
            print('error')

acaunt1 = User(input('Введите имя: '), input('Введите фамилию: '), input('Введите логин: '), input('Введите пароль: '))

acaunt1.get_public_user_name()
acaunt1.get_public_user_surname()
acaunt1.get_public_user_login()
acaunt1.get_public_user_password()
# acaunt1.get_protected_user_name()
# acaunt1.get_protected_user_surname()
# acaunt1.get_protected_user_login()
# acaunt1.get_protected_user_password()
# acaunt1.__get_private_user_name()
# acaunt1.__get_private_user_surname()
# acaunt1.__get_private_user_login()
# acaunt1.__get_private_user_password()
# print(acaunt1.get_private_user_name())
# print(acaunt1.get_private_user_surname())
# print(acaunt1.get_private_user_login())
# print(acaunt1.get_private_user_password())
print(dir())




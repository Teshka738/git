class UserAccount():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return(password == self.__password)

new_account = UserAccount("Vova","vova@mail.ru","qwerty")

print(new_account.check_password("1234"))
print(new_account.check_password("qwerty"))

new_account.set_password("1234")

print(new_account.check_password("1234"))
print(new_account.check_password("qwerty"))


class User:

 

    def __init__(self, email):

        self.__email = email


    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    
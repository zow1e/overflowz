
class User:

    def __init__(self, email):

        self.__email = email
        self.__dates = []
        self.__utilities = []
        self.__transport = []
        self.__food = []
        self.__others = []
        self.__total = []
        

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_date(self):
        return self.__dates
    def set_date(self, dates):
        self.__dates.append(dates)
    
    def get_utilities(self):
        return self.__utilities
    def set_utilities(self, utilities):
        self.__utilities.append(utilities)
    
    def get_transport(self):
        return self.__transport
    def set_transport(self, transport):
        self.__transport.append(transport)
    
    def get_food(self):
        return self.__food
    def set_food(self, food):
        self.__food.append(food)
    
    def get_others(self):
        return self.__others
    def set_others(self, others):
        self.__others.append(others)

    def get_total(self):
        return self.__total
    def set_total(self, total):
        self.__total.append(total)
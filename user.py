
class User:

    form = 0

    def __init__(self, email):


        self.__email = email
        self.__utilities = []
        self.__transport = []
        self.__food = []
        self.__others = []
        self.__total = []
        self.__formlist = []
        self.__stats = []
        
        
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    
    def get_utilities(self):
        return self.__utilities
    def set_utilities(self, utilities):
        self.__utilities.append(utilities)
    def delete_utilities(self, no):
        self.__utilities.pop(no)
    
    def get_transport(self):
        return self.__transport
    def set_transport(self, transport):
        self.__transport.append(transport)
    def delete__transport(self, no):
        self.__transport.pop(no)
    
    def get_food(self):
        return self.__food
    def set_food(self, food):
        self.__food.append(food)
    def delete__food(self, no):
        self.__food.pop(no)
    
    def get_others(self):
        return self.__others
    def set_others(self, others):
        self.__others.append(others)
    def delete__others(self, no):
        self.__others.pop(no)

    def get_total(self):
        return self.__total
    def set_total(self, total):
        self.__total.append(total)
    def delete__total(self, no):
        self.__total.pop(no)

    def get_formid(self):
        return self.__formlist

    def set_formid(self):
        User.form += 1
        self.__formlist.append(User.form)

    def delete_formid(self, no):
        self.__formlist.pop(no)

            
    def get_stats(self):
        return self.__stats
    def set_stats(self,stats):
        self.__stats.append(stats)
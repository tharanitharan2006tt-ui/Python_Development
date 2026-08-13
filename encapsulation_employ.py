class Employee:
    def __init__(self,name):
        self.__designation = "software developer"
        self.__name = name
    def set_promote(self,new_designation):
        self.__designation = new_designation
        print("promation approved")
    def get_promote(self):
        return self.__designation
E =Employee("")
E.set_promote("senior developer")
E.get_promote()
# print(E.__designation)


class Mobile:
    def __init__(self):
        self.__mobile = 9791558097
    def set_mobile(self,new_mobile):
        self.__mobile = new_mobile
    def get_mobile(self):
        return self.__mobile
M = Mobile()
M.set_mobile(6383253531)
print(M.get_mobile())
M.set_mobile(8825537396)
print(M.get_mobile())
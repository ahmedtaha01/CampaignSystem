import re
from UserRegisterFileHandler import UserRegisterFileController
from trait import invalid

class RegisterController:

    def __init__(self):
        self.first_name = self.__firstNameCaller('enter your first name : ')
        self.last_name = self.__lastNameCaller('enter your last name : ')
        self.email = self.__emailCaller('enter your email : ')
        self.phone = self.__phoneCaller('enter your phone number : ')
        self.password = self.__passwordCaller('enter your password : ')
        self.confirm_password = self.__confirmPasswordCaller('confirm your password : ')
        UserRegisterFileController.add(self.changeToList())

    def changeToList(self):
        return [self.first_name,self.last_name,self.email,self.phone,self.password]

       
        
    def __firstNameCaller(self,message):
        first_name = input(message)
        if first_name.isalpha():
            return first_name
        else:
            print(invalid())
            return self.__firstNameCaller(message)   

    def __lastNameCaller(self,message):
        last_name = input(message)
        if last_name.isalpha():
            return last_name
        else:
            print(invalid())
            return self.__lastNameCaller(message)

    def __emailCaller(self,message):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input(message)
        if(re.fullmatch(regex, email)):
            return email
        else:
            print(invalid())
            return self.__emailCaller(message)

    def __phoneCaller(self,message):
        phone = input(message)
        if len(phone) == 12:
            return phone
        else:
            print(invalid())
            print('phone number must start with number : 2 and its length is 12')
            return self.__phoneCaller(message)


    def __passwordCaller(self,message):
        password = input(message)
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        if(re.fullmatch(regex, password)):
            return password
        else:
            print(invalid())
            print('''            Password should have at least one number ,
            one uppercase and one lowercase character ,
            one special symbol ,
            Should be between 6 to 20 characters long.''')
            return self.__passwordCaller(message)


    def __confirmPasswordCaller(self,message):
        confirm_password = input(message)
        if(confirm_password == self.password):
            return confirm_password
        else:
            print(invalid())
            return self.__confirmPasswordCaller(message)     


    def show(self):
        print('here is your data')
        print(f"first name = {self.first_name}")
        print(f"last name = {self.last_name}")
        print(f"email = {self.email}")
        print(f"phone number = {self.phone}")
        print(f"password = {self.password}")



                     



       

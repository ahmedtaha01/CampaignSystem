import re
from trait import invalid
from UserLoginFileHandler import UserLoginFileController

class Login:
    def __init__(self):
        email = self.__emailCaller('enter your email : ')
        password = self.__passwordCaller('enter your password : ')
        self.list = UserLoginFileController.giveLiscence([email,password])
        


    def __emailCaller(self,message):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input(message)
        if email == 'quit':
            return
        if(re.fullmatch(regex, email)):
            return email
        else:
            print(invalid())
            return self.__emailCaller(message)    

    def __passwordCaller(self,message):
        password = input(message)
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        if password == 'quit':
            return
        if(re.fullmatch(regex, password)):
            return password
        else:
            print(invalid())
            print('''            Password should have at least one number ,
            one uppercase and one lowercase character ,
            one special symbol ,
            Should be between 6 to 20 characters long.''')
            return self.__passwordCaller(message)        
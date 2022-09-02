
from FileWriteHandler import FileWriteController
from FileReadHandler import FileReadController
from trait import fromListToString

class UserRegisterFileController:

    def add(list):
        id = FileReadController.lastIdNumber('users_file.txt')
        list.insert(0,id)
        
        strs = fromListToString(list)
        FileWriteController.addToFile(strs,'users_file.txt')

       



    
           

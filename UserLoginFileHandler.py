from FileReadHandler import FileReadController

class UserLoginFileController:
    
    def giveLiscence(list):
        data = FileReadController.dataFromFile('users_file.txt')
        for line in data:
            columns = line.split(':')
            if list[0] == columns[3] and list[1] == columns[5][:-1]:
                return columns

        return False    
        

        
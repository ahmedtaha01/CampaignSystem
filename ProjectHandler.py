from trait import fromListToString
from FileReadHandler import FileReadController
from FileWriteHandler import FileWriteController
import datetime

class ProjectController:


    def add(projectList):
        
        id = FileReadController.lastIdNumber('projects_file.txt')
        projectList.insert(0,id)
        strs = fromListToString(projectList)
        

        FileWriteController.addToFile(strs,'projects_file.txt')


    def view():
        return FileReadController.dataFromFile('projects_file.txt')    

    def search(name):
        data = ProjectController.view()
        for index,line in enumerate(data):
            columns = line.split(':')
            if name == columns[1]:
                return data[index]
                
        return False

    def delete(project_id,person_id):
        
        data = ProjectController.view()
        for index,line in enumerate(data):
            columns = line.split(':')
            if project_id == columns[0]:
                if person_id == columns[5][:-1]:
                    del data[index]
                    FileWriteController.writeToFile(data,'projects_file.txt')
                    return 'deleted successfully'
                else:
                    return 'you cannt delete this project'
                
        return 'not found'
    

    def update(project_id,person_id):
        data = ProjectController.view()
        for index,line in enumerate(data):
            columns = line.split(':')
            if project_id == columns[0]:
                if person_id == columns[5][:-1]:
                    ProjectController.__updateRow(data,index)
                    return 'updated successfully'
                else:
                    return 'you cannt update this project'
                
        return 'not found'

    def __updateRow(data,index):
        title = input('enter new title : ')
        details = input('enter new details : ')
        target = input('enter new target : ')
        date = ProjectController.__timeCaller('enter new start and end time : ')
        columns = data[index].split(':')
        strs = fromListToString([columns[0],title,details,target,date,columns[5]])
        data[index] = strs
        FileWriteController.writeToFile(data,'projects_file.txt')

    def __timeCaller(message):
        TimeArr =[]
        time = input(message)
        for i in time.split():
            try:
                datetime.datetime.strptime(i, '%Y-%m-%d')
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD")
                return ProjectController.__timeCaller(message)
        
        TimeArr.append(time.split())    

        return TimeArr    


            


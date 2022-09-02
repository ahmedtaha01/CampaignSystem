from bdb import Breakpoint
from trait import invalid
import datetime
from ProjectHandler import ProjectController

class FundingSystem:

    def __init__(self,person):
        self.person = person        #composition
        while True:
            print('Welcome to the funding system how can we help you')
            
            choice = input('1 - to view all campaign projects enter : view \n'
                        '2 -  to create a new campaign enter : create \n'
                        '3 - to delete a campaign enter : delete \n'
                        '4 - to update a campaign enter : update \n'
                        '5 - to search for sepcific campagin enter name of campaign : \n')

            if choice == 'create':
                self.createNewProject()
            elif choice == 'view':
                self.viewProjects()
            elif choice == 'delete':
                self.deleteProject('enter the project id you want to delete : ')
            elif choice == 'update':
                self.updateProject('enter the project id you want to update : ')
            elif choice == 'search':
                self.searchProject('enter the project name you want to search : ')       
            elif choice == 'quit':
                break
            else:
                print('this is not a choice')
            
    
    def searchProject(self,message):
        project_name = input(message)
        data = ProjectController.search(project_name)
        if data:
            columns = data.split(':')
            for i in columns:
                print(i +'\t',end='')
        else:
            print('no name like this')    


    def viewProjects(self):
        data = ProjectController.view()
        print('id \t name \t description \t target \t start date \t end date \t userId')
        for line in data:
            columns = line.split(':')
            for column in columns:        
                print(column +'\t',end='')
            print('\n')    

    def deleteProject(self,message):
        project_id = input(message)
        state = ProjectController.delete(project_id,self.person[0])
        print(state)    
           
    def updateProject(self,message):
        project_id = input(message)
        state  = ProjectController.update(project_id,self.person[0])
        print(state)             

               

    def createNewProject(self):
        self.title = self.__titleCaller('enter the title : ')
        self.details = self.__detailsCaller('enter the details : ')
        self.target = self.__targetCaller('enter the target (max:250000) : ')
        self.time = self.__timeCaller('enter the start and end date time : ')
        ProjectController.add(self.changeToList())

    def changeToList(self):
        return [self.title,self.details,self.target,self.time,self.person[0]] #id

       

    def __titleCaller(self, message):
        title = input(message)
        if all(x.isalpha() or x.isspace() for x in title):
            return title
        else:
            print(invalid())
            return self.__titleCaller(message)

    def __detailsCaller(self, message):
        details = input(message)
        if all(x.isalpha() or x.isspace() for x in details):
            return details
        else:
            print(invalid())
            return self.__detailsCaller(message)

    def __targetCaller(self, message):
        target = input(message)
        if target.isdigit() and int(target) < 250000:
            return target
        else:
            print(invalid())
            return self.__targetCaller(message)

    def __timeCaller(self, message):
        TimeArr =[]
        time = input(message)
        for i in time.split():
            try:
                datetime.datetime.strptime(i, '%Y-%m-%d')
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD")
                return self.__timeCaller(message)
        
        TimeArr.append(time.split())    

        return TimeArr


        


class FileWriteController():


    def addToFile(strs,filename):
        try:
            file=open(filename,'a')
            file.write(strs + '\n')
        except:
            print('error with openeing file')

    def writeToFile(strs,filename):
        try:
            file=open(filename,'w')
            for line in strs:
                file.write(line)
        except:
            print('error with openeing file')
           

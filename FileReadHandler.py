import os
class FileReadController():

    def lastIdNumber(filename):
        # if file is empty
        if os.stat(filename).st_size == 0:
            return int(1)

        try:
            file = open(filename,'r')
        except:
            print('error with opeening file')

        for l in file:
            pass
        
        last_line = l
        vars = last_line.split(':')

        return int(vars[0])+1

    def dataFromFile(filename):
        try:
            file = open(filename,'r')
        except:
            print('error with opening file')

        return file.readlines()
        


def fromListToString(datalist):
        strs = ""
        for i in datalist:
            if isinstance(i,list):
                for j in i:
                    strs += str(j) +':'
            else:                
                strs += str(i) +':'

        return strs[:-1]


def invalid():
    return 'invalid input' 
        
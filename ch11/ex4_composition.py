class ReverseFile:

    def __init__(self, filename, mode='r'):
        self.__f = open(filename, mode)
        
    def write(self, line):
        self.__f.write(line[::-1])
        
    def close(self):
        self.__f.close()
    
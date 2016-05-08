import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(list,Loggable):
    def append(self,n):
        x = super(LoggableList,self).append(n)
        z = super(LoggableList, self).log(n)
        return z
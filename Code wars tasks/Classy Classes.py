class Person:
    def __init__(self,name,age):
        self.info= "%ss age is %d" %(name,age)
    def your_info(self):
        print(self.info)
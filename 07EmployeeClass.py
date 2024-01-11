#wap to create employee class
class Employee:
    def __init__(self):
        employee={'Id':1,'Name':'pankaj','Gender':'male','City':'delhi','Salary':55000}
        for i in employee:
            print(i,":",employee[i])
obj=Employee()

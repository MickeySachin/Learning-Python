# 23th March 2023
# Modules

class stuMethods:

    def getData(self):
        flag = 1

        while flag != 0:
            self.id.append(input("Enter Student Id = "))
            self.name.append(input("Enter Student Name = "))
            self.rollno.append(input("Enter Student Rollno = "))
            flag = int(input("Enter 1 to add new detail while 0 to exit = "))
            self.countEntries += 1


    def printColumnHeading(self):
        print("Id - Name - Rollno")


    def printData(self, count):
        count = self.countEntries

        for i in range(count):
            print(f' {self.id[i]} - {self.name[i]} - {self.rollno[i]}')



class basicOperations:

    def addition(x, y):
        return x + y
     
    def subtraction(x, y):
        return x - y
    
    def multiplication(x, y):
        return x * y
    
    def division(x, y):
        return x / y





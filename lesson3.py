class Student:
    studentsCounter = 0
    def __init__(self, name, progress, birthday, school = "NVK №2"):
        self.name = name
        self.progress = progress
        self.DateOfBirthday = birthday
        self.school = school
        Student.studentsCounter += 1

    def __str__(self):
        return f"№ {self.studentsCounter}: \n Name: {self.name} \n progress: {self.progress} \n birthday: {self.DateOfBirthday} \n school №: {self.school}"

    def addProgress(self, a):
        self.progress += a
        print(self.progress)

    def method(self):
        print("method")


class Human:
    def __init__(self, name = "Human"):
        self.name = name
class Auto():
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def addPassengers(self, human):
        self.passengers.append(human)
    def printPassengersNames(self):
        if self.passengers != []:
            print(f"Brand: {self.brand}, passengers:")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"there are no passengers in {self.brand}")
Oleg = Human("Oleg")
Oksana = Human("Oksana")
car = Auto("Mercedes")
car.addPassengers(Oleg)
car.addPassengers(Oksana)
car.printPassengersNames()






input("Press {enter}")

# Sasha = Student("Sasha", 10, "02.11.2010")
# print(Sasha)
# input()
# Vika = Student("Vika", 12, "11.10.2009")
# print(Vika)
# input()
# Vanya = Student("Vanya", 9, "05.01.2011")
# print(Vanya)
# input()
#
# print("")
#
# print("Students:", Student.studentsCounter)
class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    def getCity(self):
        return self.__city

    def getStreet(self):
        return self.__street

    def getNumber(self):
        return self.__number

class Person:
    def __init__(self, name, city, street, number):
        self.__name = name
        self.__address = Address(city, street, number)

    def getName(self):
        return self.__name
    
    def getCity(self):
        return self.__address.getCity()
    
    def getStreet(self):
        return self.__address.getStreet()
    
    def getNumber(self):
        return self.__address.getNumber()

class MarkBook:
    __grades = {}

    def addMark(self, subject, mark):
        if subject not in self.__grades:
            self.__grades[subject] = list([])
        self.__grades[subject].append(mark)

    def getMarks(self, subject):
        return self.__grades[subject]

    def getAverage(self, subject):
        return sum(self.__grades[subject]) / len(self.__grades[subject])

class Computer:
    def __init__(self, mark, year, cpu, os, ram, disk):
        self.__mark = mark
        self.__year = year
        self.__cpu = cpu
        self.__os = os
        self.__ram = ram
        self.__disk = disk

    def getMark():
        return self.__mark     
    
    def getYear():
        return self.__year
    
    def getCpu():
        return self.__cpu
    
    def getOs():
        return self.__os
    
    def getRam():
        return self.__ram
    
    def getDisk():
        return self.__disk    
    
    def printComputer(self):
        print(self.__mark)
        print(self.__year)
        print(self.__cpu)
        print(self.__os)
        print(self.__ram)
        print(self.__disk)

class Student(Person):
    def __init__(self, person):
        super(Student, self).__init__(person.getName(), person.getCity(), person.getStreet(), person.getNumber())
        self.__markbook = MarkBook()
        self.__computer = Computer("Acer", 2016, 25, "windows", 8, 1024)

    def myAddMark(self, subject, grade):
        self.__markbook.addMark(subject, grade)

    def printStudent(self):
        print(super().getName())
        print(super().getCity())
        print(super().getStreet())
        print(super().getNumber())
        print(self.__markbook.getMarks("TP"))
        print(self.__markbook.getAverage("TP"))
        self.__computer.printComputer()

person = Person("Simeon", "Sofia", "Lerin", 14)
student = Student(person)

student.myAddMark("TP", 6)
student.myAddMark("TP", 5)
student.myAddMark("TP", 4)
student.printStudent()

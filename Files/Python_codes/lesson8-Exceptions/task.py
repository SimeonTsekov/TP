class InvalidNumberException(Exception):
    pass

class Students:
    def __init__(self):
        self.__students = {1:"Dio", 2:"Jonathan", 3:"Joseph", 4:"Jotaro"}

    def get_name(self, student_number):
        if(self.__students.get(student_number) == None): 
            raise InvalidNumberException

        name = self.__students.get(student_number)
        print(name)

students = Students()
try:
    students.get_name(1)
    students.get_name(2)
    students.get_name(3)
    students.get_name(4)
    students.get_name(5)
except InvalidNumberException:
    print("The number does not exist.")

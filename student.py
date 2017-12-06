from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,title):
        self.modules.append(title)
        self.grades[title] = title.get_grade()

    def get_list_modules(self):
        print("Modules of Student "+self.name)
        for module in self.modules:
            print("\t"+module.get_title())

    def get_grades(self):
        print("Grades of Student "+self.name)
        for element in self.grades.keys():
            print("\t"+element.get_title()+": "+str(self.grades[element]))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6


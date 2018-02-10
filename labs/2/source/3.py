#!/usr/bin/python3
# Lab assignment 2: part 3


class Person:
    """
    Person class. Each person will have name and age.
    """
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    @staticmethod
    def get_person_count():
        # Static method for counting the number of Person objects
        return Person.count

    def __repr__(self):
        return "Name: " + self.name + "\n" + "Age: " + str(self.age)


class Student(Person):
    """
    Student class. It is inheriting from Person class with additional attribute 'id'.
    """
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.student_id = id

    def __repr__(self):
        return super().__repr__() + "\n" + "Student ID: " + str(self.student_id)


class Job:
    """
    Job class. Each job will have title and salary.
    """
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

    def __repr__(self):
        return "Title: " + self.title + "\n" + "Salary: $" + str(self.salary)


class Librarian(Person, Job):
    """
    Librarian class. It is inheriting from both Person and Job classes with additional attribute 'id'.
    """
    def __init__(self, name, age, title, salary, id):
        Person.__init__(self, name, age)
        Job.__init__(self, title, salary)
        self.librarian_id = id

    def __repr__(self):
        return Person.__repr__(self) + "\n" + Job.__repr__(self) + "\n" + "Librarian ID:" + str(self.librarian_id)


class Book:
    """
    Book class. Each book will have name, author, and a private variable 'secret'.
    """
    def __init__(self, name, author, secret):
        self.name = name
        self.author = author
        self.__secret = secret

    def __repr__(self):
        return "Name: " + self.name + "\n" + "Author: " + self.author + "\n" + "Secret: " + self.__secret


print("=================================Person class=================================")
person1 = Person("Test person", 1)
print(person1)
print("==============================================================================")
print()
print("==============Student class(inheritance from Person + super call)=============")
student1 = Student("John Bob", 18, 123789)
print(student1)
print("==============================================================================")
print()
print("==================================Job class===================================")
job1 = Job("Librarian 2A", 50000.00)
print(job1)
print("==============================================================================")
print()
print("===Librarian class(multiple inheritances from Person and Job + super calls)===")
librarian1 = Librarian("librarian1", 30, "Librarian Staff", 50000.00, 123154)
print(librarian1)
print("==============================================================================")
print()
print("=====================Book class (private secret variable)=====================")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "secret 1")
print(book1)
print("Private variable visible:", hasattr(book1, "__secret"))
print("==============================================================================")

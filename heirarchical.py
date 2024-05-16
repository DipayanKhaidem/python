class Student:
    def display(self):
        print("Usn:", self.usn)
        print("Name:", self.name)
        print("Age:", self.age)

class PgStudent(Student):
    def getData(self):
        self.usn = int(input("Enter usn id: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.sem = int(input("Enter sem: "))
        self.stipend = int(input("Enter stipend: "))

    def display(self):
        print("++++PG Student++++")
        print("Usn is", self.usn)
        print("Name is", self.name)
        print("Age is", self.age)
        print("Sem is", self.sem)
        print("Stipend is", self.stipend)

class UgStudent(Student):
    def getData(self):
        self.usn = int(input("Enter usn id: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.sem = int(input("Enter sem: "))
        self.stipend = int(input("Enter stipend: "))

    def display(self):
        print("++++UG Student++++")
        print("Usn is", self.usn)
        print("Name is", self.name)
        print("Age is", self.age)
        print("Sem is", self.sem)
        print("Stipend is", self.stipend)

p1 = PgStudent()
u1 = UgStudent()

while True:
    print("1.PG Student\n2.UG Student")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("1.Get Data\n2.Show data")
        op = int(input("Enter your choice: "))
        if op == 1:
            p1.getData()
        elif op == 2:
            p1.display()
        else:
            break
    elif ch == 2:
        print("1.Get Data\n2.Show data")
        op = int(input("Enter your choice: "))
        if op == 1:
            u1.getData()
        elif op == 2:
            u1.display()
        else:
            break

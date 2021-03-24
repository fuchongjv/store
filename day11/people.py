class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def show(self):
        print(self.name, self.age, self.sex)


class Work(People):
    pass


class Student(Work):

    def __init__(self, name, age, sex, num):
        super().__init__(name, age, sex)
        self.get__Num = num

    def setNum(self, num):
        pass

    def getNum(self):
        return self.get__Num

    def student(self):
        print("在学习")

    def sing(self):
        print("在唱歌")

    def show(self):
        super().show()
        print(self.get__Num)


class Worker(Work):
    def work(self):
        print("在干活")

    def show(self):
        super().show()


a = People("张三", 21, "男")
a.show()
b = Student("王一", 22, "男", 4)
b.setNum(9)
b.show()
b.student()
b.sing()
c = Worker("李四", 23, "男")
c.show()
c.work()
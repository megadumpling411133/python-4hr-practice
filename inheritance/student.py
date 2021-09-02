# 用 student 來繼承 Person 內相同的部分
# from person (就是person.py) import Person (person.py 定義的 class > Person) 引入 不同檔案
# class student(person):
# 相當於 person.py 中 複製 class Person 裡面內容 到 student 這個類別內的最上面
# 因為完成繼承 此時 重複的程式碼內容就可以刪去了 > name age (line 13 - line 17) > 程式碼縮減
from person import Person
class Student(Person):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
    # 繼承精簡程式碼
    # def print_name(self):
    #     print(self.name)

    # def print_age(self):
    #     print(self.age)
    # 繼承精簡程式碼
    def print_school(self):
        print(self.school)
    
#---------------------相當於下方-----------------------
# from person import Person
# class Student(Person):
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#    
#    def print_name(self):
#        print(self.name)
#
#    def print_age(self):
#        print(self.age)
#
#    def __init__(self, name, age, school): 
# 後面的初始函式__init__ 會覆蓋前面的__init__初始函式
# 保持初始函式只有一個
#        self.name = name
#        self.age = age
#        self.school = school
    # 繼承精簡程式碼
    # def print_name(self):
    #     print(self.name)

    # def print_age(self):
    #     print(self.age)
    # 繼承精簡程式碼
#   def print_school(self):
#        print(self.school)  
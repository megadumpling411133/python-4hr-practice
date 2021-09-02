# inheritance 繼承
# 來減少程式碼
from student import Student

student1 = Student("David", 31, "QQ工程師學校QQ")
student1.print_name() # 來自class Student 繼承自 class Person 定義的函式
student1.print_age() # 來自class Student 繼承自 class Person 定義的函式
student1.print_school() # 來自class Student 定義的函式 
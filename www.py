class Student:
    def __init__(self, name, age, grade):
        """初始化学生对象"""
        self.name = name  # 学生姓名
        self.age = age    # 学生年龄
        self.grade = grade  # 学生年级

    def introduce(self):
        """自我介绍"""
        return f"大家好，我叫{self.name}，我{self.age}岁，正在读{self.grade}年级。"

    def study(self, subject):
        """学习科目"""
        return f"{self.name}正在学习{subject}。"

# 创建学生对象
student1 = Student("小明", 15, "9")
student2 = Student("小红", 14, "8")

# 使用对象的方法
print(student1.introduce())
print(student2.introduce())
print(student1.study("数学"))
print(student2.study("英语"))

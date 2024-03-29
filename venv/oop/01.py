'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
# 一个空类，pass代表直接跳过
# 此处pass必须有
    pass
# 定义一个对象
mingyue = Student()

# 在定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 20
    course = 'python'

    # 需要注意
    # 1. def doHomework的缩进层级
    # 2. 系统默认由一个self参数
    def doHomework(self):
        print("I 在做作业")

        # 推荐在函数末尾使用return
        return None

# 实例化
yueyue = PythonStudent()
print(yueyue.age)
print(yueyue.name)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()
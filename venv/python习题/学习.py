import math
# print(math)  指在该代码中中引用了其他math模块 数学模块
# celi() 向上取整操作
# print(math.ceil(5.01))    #ceil 表示进1取整法
# print(math.ceil(6.1))

# floor() 向下取整   减1取整法
# print(math.floor(5.9))
# print(math.floor(5.1))

# 查看保留的关键字  是不可以用来当做变量命名的
# import keyword
# # print(keyword.kwlist)

# # round () 四舍五入函数  pyhton内置函数
# print(round(3.7))
# print(round(5.1))
#
# # sqrt() 开平方
# print(math.sqrt(9))
# print(math.sqrt(879))

# pow() 跟幂运算差不多，计算一个数的几次方  有两个参数，第一个是底数，第二个是指数
# print(math.pow(99,2))  # 99的二次方
# print(math.pow(3,4))   # 3的4次方
# #  函数计算返回浮点型  幂运算返回整形 3**4
# print(4**3)

# fabs() 对一个数值获取其绝对值  返回的浮点数
# print(math.fabs(-2))
# print(math.fabs(7.7))
# print(math.fabs(0.3))

# abs() 也是获取绝对值操作  不是数学模块的 是python内置的模块  返回值由本身的类型而定  本身是浮点就是浮点 本身是整形就返回浮点型
# print(abs(33.3))
# print(abs(-33))
# print(abs(0))

# fsum（） 求和  是math模块   返回的是浮点数
# print(math.fsum([3,4,5,6,7,8,9]))
#
# # sum  是python内置模块  返回的是整形
# print(sum([2,3,4,5,6,7,8]))

# math.modf math的函数  作用是将一个浮点数拆分为整数部分和小数部分组成元组  小数在前 整数在后
# print(math.modf(3.4))
# print(math.modf(3.5))
# help(math.modf)

# math.copysign()   将第二个数的符号（正负号）传给第一个数  返回第一个数字的浮点数
# print(math.copysign(2,-2))
# print(math.copysign(-2,3))

# #  打印自然对数e和π的值
# print(math.e)
# print(math.pi)

import random
# # random()获取0-1之间的随机小数 包含0不包含1
# for i in range(10):
    # print(random.random())    #随机小数 0-1  包含0
    # 随机指定开始和结束之间的值
    # print(random.randint(1,9))  #左右都包括  获取整形值
    # random.randrange() 获取指定开始和结束的值，可以指定间隔值
    # print(random.randrange(1,9,2))  #右好像不包括

# choice()随机获取列表中的值
# print(random.choice([2,34,5,6,66,77]))

# shuffle() 随机打乱序列  返回值是None
# print(random.shuffle([2,3,3444,555,666]))
# list1 = [1,2,3,4343,545,45,44,66]
# print(random.shuffle(list1))
# print(list1)

# uniform()  随机获取指定范围内的值（包括小数）
print(random.uniform(2,9))

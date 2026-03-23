# =====================
# 函数基础
# =====================

# 1. 简单函数

def greet():
    """问候函数"""
    print("Hello! 您好!")

greet()

# 2. 带参数的函数
def greet_person(name):
    """带参数的问候"""
    print(f"Hello, {name}")

greet_person("张三")
greet_person("李四")

# 3. 带返回值的函数
def add(a, b):
    """加法"""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# 4. 默认函数
def greet_with_title(name, title="先生"):
    """带默认参数"""
    return f"您好， {title}{name}!"

print(greet_with_title("张三"))
print(greet_with_title("李四", "女士"))
print(greet_with_title("王五", "博士"))

# 5. 返回多个值
def get_stats(numbers):
    """返回多个统计值"""
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

total, avg = get_stats([10, 20, 30, 40, 50])
print(f"总和: {total}, 平均: {avg}")

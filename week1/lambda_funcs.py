# =====================
# 可变参数
# =====================

# 1. *args - 可变位置参数
def sum_all(*numbers):
    """求和"""
    total = 0
    for n in numbers:
        total += n
    return total

print(f"求和: {sum_all(1, 2, 3)}")           # 6
print(f"求和: {sum_all(10, 20, 30, 40, 50)}") # 150

# 2. **kwargs - 可变关键字参数
def print_info(**info):
    """打印信息"""
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n个人信息:")
print_info(name="张三", age=25, city="北京")

# 3. 组合使用
def func(*args, **kwargs):
    """组合"""
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

func(1, 2, 3, name="张三", age=25)

# =====================
# Lambda 函数
# =====================

print("\n=== Lambda 函数 ===")

# 简单 lambda
square = lambda x: x ** 2
print(f"5的平方: {square(5)}")

# 多参数lambda
add = lambda a, b: a + b
print(f"3 + 7 = {add(3,7)}")

# 配置内置函数使用
numbers = [5, 2, 8, 1, 9, 3]

# sorted with lambda
sorted_nums = sorted(numbers)
print(f"排序: {sorted_nums}")

# 按字典的某个key排序
students = [
    {"name": "张三", "score": 90},
    {"name": "李四", "score": 85},
    {"name": "王五", "score": 92},
]

sorted_students = sorted(students, key = lambda x: x["score"], reverse=True)
print("\n按分数排序")
for s in sorted_students:
    print(f" {s['name']}: {s['score']}")

# map with lambda
names = ["alice", "bob", "charlie"]
capitalized = list(map(lambda x: x.capitalize(), names))
print(f"\n首字母大写: {capitalized}")

# filter with lambda
scores = [90, 45, 78, 88, 55, 92]
passing = list(filter(lambda x: x >= 60, scores))
print(f"及格分数: {passing}")


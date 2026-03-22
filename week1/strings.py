# ================
# 字符串操作
# ================

name = "Python"
text = " Hello, World! "

# 1. 字符串方法
print("=== 字符串方法 ====")
print(f"转大写: {name.upper()}")
print(f"转小写: {name.lower()}")
print(f"去空格: '{text.strip()}'")
print(f"替换: {name.replace('Py','Java')}")

# 2. 字符串格式化
print("\n=== 格式化 ===")
age = 45
price = 99.5

# f-string (推荐)
print(f"我叫{name}, 今年{age}岁")
print(f"价格: ¥{price:.2f}")

# format方法
template = "姓名: {}, 年龄: {}"
print(template.format(name, age))

# 3. 字符串切片
print("\n=== 切片 ===")
s = "Hello Python"
print(f"完整: {s}")
print(f"前5个: {s[:5]}")
print(f"后6个:{s[-6:]}")
print(f"跳过: {s[::2]}")

# ================
# 数值运算                
# ================

print("\n=== 数值运算 ===")
a, b = 10, 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} // {b} = {a // b}")  #整除
print(f"{a} % {b} = {a % b}")    #取余
print(f"{a} ** {b} = {a ** b}")

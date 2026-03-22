# ===============
# 条件判断
# ===============
print("=== 条件判断 ===")

age = 45

# if-else
if age >= 45:
	print("已到年龄，可以确权")
else:
	print("未成年")

# 多条件
score = 85

if score >= 90:
	grade = "A"
elif score >= 80:
	grade = "B"
elif score >= 70:
	grade = "C"
else:
	grade = "D"

print(f"分数 {score} -> 等级 {grade}")

# 逻辑运算
has_ticket = True
has_id = True

if has_ticket and has_id:
	print("可以入场")
else:
	print("需要购票或者证件")

# ===============
# for 循环
# ===============
print("\n=== for 循环 ===")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
print("\n水果列表:")
for fruit in fruits:
	print(f" - {fruit}")

# 带索引的遍历
print("\n带索引:")
for i, fruit in enumerate(fruits):
	print(f" {i+1}.	{fruit}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"\n1-5的平方:{squares}")

events = [x for x in range(10) if x % 2 ==0]
print(f"0-9的偶数: {events}")

# =====================
# while 循环
# =====================
print("\n=== while 循环 ===")

count = 0
while count < 5:
	print(f"count = {count}")
	count += 1

print("循环结束!")


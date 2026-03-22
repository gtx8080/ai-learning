 # =====================
 # 列表 (List)
 # =====================
 
print("=== 列表 ===")

numbers = [1, 2, 3, 4, 5]

# 访问
print(f"第一个: {numbers[0]}")
print(f"最后一个: {numbers[-1]}")

# 切片
print(f"前3个: {numbers[:3]}")

# 添加
numbers.append(6)
print(f"添加后: {numbers}")

numbers.insert(0, 0)
print(f"插入0后: {numbers}")

# 删除
numbers.pop()
print(f"pop后: {numbers}")

numbers.pop(0)
print(f"pop(0)后: {numbers}")

# 排序
scores = [90, 70, 85, 95, 80]
scores.sort()
print(f"排序后: {scores}")

scores.sort(reverse=True)
print(f"降序: {scores}")

# =====================
# 字典 (Dict)
# =====================
 
print("\n=== 字典 ===")

person = {
	"name": "张三",
	"age": 25,
	"city": "北京",
	"skills": ["Python", "JavaScript"]
}

# 访问
print(f"姓名: {person['name']}")
print(f"年龄: {person.get('age')}")
print(f"技能: {person['skills']}")

# 遍历
print("\n遍历字典:")
for key, value in person.items():
	print(f" {key}: {value}")

# 修改
person["age"] = 26
person["email"] = "zhangsan@example.com"
print(f"\n修改后: {person}")

# 常用方法
print(f"\n键: {list(person.keys())}")
print(f"值: {list(person.values())}")

# =====================
# 综合练习
# =====================

print("\n=== 成绩统计 ===")

students = [
	{"name": "张三", "score": 90},
	{"name": "李四", "score": 85},
	{"name": "王五", "score": 92},
	{"name": "赵六", "score": 78},
]

# 计算平均分
total = sum(s["score"] for s in students)
avg = total / len(students)
print(f"平均分: {avg:.1f}")

# 找最高分
best = max(students, key=lambda x: x["score"])
print(f"最高分: {best['name']} - {best['score']}")

# 及格名单
passing = [s['name'] for s in students if s['score'] >= 80]
print(f"及格: {passing}")


# =====================
# 模块导入
# =====================

# 1. 导入标准库
import math

print(f"圆周率: {math.pi}")
print(f"平方根: {math.sqrt(16)}")
print(f"2的3次方: {math.pow(2, 3)}")

# 2. 导入特定函数
from datetime import datetime, timedelta

now = datetime.now()
print(f"\n当前时间: {now}")

# 7天后的日期
future = now + timedelta(days=7)
print(f"7天后: {future.strftime('%Y-%m-%d')}")

# 3. 使用 as 给模块起别名
import random as rnd

print(f"\n随机整数: {rnd.randint(1, 100)}")
print(f"随机选择: {rnd.choice(['苹果', '香蕉', '橙子'])}")

# 洗牌
cards = ['A', '2', '3', '4', '5']
rnd.shuffle(cards)
print(f"洗牌后: {cards}")

# 4. 导入自己写的模块
# 先创建一个简单的工具模块
print("\n=== 创建自己的模块 ===")

# 创建 utils.py
# 注意：这里用字符串模拟创建，实际执行时先运行上面的创建命令

# 5. 查看模块内容
print("\n可用的数学函数:")
print([x for x in dir(math) if not x.startswith('_')])

# 6. json 模块
import json

data = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "AI"]
}

# 字典转 JSON 字符串
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(f"\nJSON字符串:\n{json_str}")

# JSON 字符串转字典
parsed = json.loads(json_str)
print(f"\n解析后: {parsed}")

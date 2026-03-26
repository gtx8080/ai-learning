# =====================
# Python requests 实战
# =====================

import requests
import json

print("=== Python Requests 实战 ===\n")

# 1. GET 请求
print("1. GET 请求 - 获取用户信息")
print("-" * 40)

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(f"状态码: {response.status_code}")
print(f"响应内容:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# 2. GET 带参数
print("\n2. GET 带查询参数")
print("-" * 40)

params = {
    "userId": 1,
    "completed": "false"
}
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params=params
)
todos = response.json()
print(f"找到 {len(todos)} 条待办事项")
for todo in todos[:3]:
    print(f"  - {todo['id']}: {todo['title']}")

# 3. POST 请求
print("\n3. POST 请求 - 创建用户")
print("-" * 40)

new_user = {
    "name": "张三",
    "username": "zhangsan",
    "email": "zhangsan@example.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=new_user
)
print(f"状态码: {response.status_code}")
print(f"创建的用户:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# 4. PUT 请求
print("\n4. PUT 请求 - 更新用户")
print("-" * 40)

updated_user = {
    "id": 1,
    "name": "张三(已更新)",
    "email": "updated@example.com"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json=updated_user
)
print(f"状态码: {response.status_code}")

# 5. DELETE 请求
print("\n5. DELETE 请求 - 删除用户")
print("-" * 40)

response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/1"
)
print(f"状态码: {response.status_code}")

# 6. 错误处理
print("\n6. 错误处理")
print("-" * 40)

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/999",
        timeout=5
    )
    response.raise_for_status()  # 检查4xx/5xx错误
    print(f"响应: {response.json()}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP错误: {e}")
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")

# 7. 查看响应信息
print("\n7. 响应信息")
print("-" * 40)

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(f"状态码: {response.status_code}")
print(f"响应头: {dict(response.headers)}")
print(f"编码: {response.encoding}")
print(f"内容类型: {response.headers.get('Content-Type')}")

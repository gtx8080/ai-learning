# =====================
# FastAPI 第一个应用
# =====================

from fastapi import FastAPI

# 创建 FastAPI 应用
app = FastAPI(
    title="我的第一个API",
    description="这是一个简单的 FastAPI 示例",
    version="1.0.0"
)

# 模拟数据库
users_db = [
    {"id": 1, "name": "张三", "email": "zhangsan@example.com", "age": 25},
    {"id": 2, "name": "李四", "email": "lisi@example.com", "age": 30},
    {"id": 3, "name": "王五", "email": "wangwu@example.com", "age": 28},
]

# =====================
# GET 请求
# =====================

@app.get("/")
def read_root():
    """根路径"""
    return {
        "message": "欢迎使用 FastAPI!",
        "docs": "访问 /docs 查看API文档",
        "version": "1.0.0"
    }

@app.get("/users")
def get_users():
    """获取所有用户"""
    return {
        "total": len(users_db),
        "users": users_db
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """获取单个用户"""
    for user in users_db:
        if user["id"] == user_id:
            return user
    return {"error": "用户不存在"}

@app.get("/users/search")
def search_users(name: str = None, age: int = None):
    """搜索用户"""          # ← 这里已经确认成对
    results = users_db

    if name:
        results = [u for u in results if name.lower() in u["name"].lower()]

    if age:
        results = [u for u in results if u["age"] == age]

    return {"results": results, "count": len(results)}

# =====================
# 测试
# =====================

if __name__ == "__main__":
    print("=" * 50)
    print("FastAPI 应用已创建!")
    print("=" * 50)
    print("\n启动方式:")
    print("  uvicorn first_api:app --reload")
    print("\n访问:")
    print("  - API文档: http://localhost:8000/docs")
    print("  - 根路径: http://localhost:8000/")
    print("  - 用户列表: http://localhost:8000/users")
    print("=" * 50)

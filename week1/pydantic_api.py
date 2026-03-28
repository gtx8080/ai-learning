# =====================
  # FastAPI + Pydantic
  # =====================

  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel, EmailStr, Field, validator
  from typing import Optional, List
  from datetime import datetime  app = FastAPI(title="Pydantic API 示例")  # =====================
  # Pydantic 模型
  # =====================

  class UserBase(BaseModel):
      """用户基础模型"""
      name: str = Field(..., min_length=1, max_length=50)
      email: EmailStr  # 邮箱格式验证
      age: Optional[int] = Field(None, ge=0, le=150)  class UserCreate(UserBase):
      """创建用户"""
      password: str = Field(..., min_length=6)  @validator('name')
  def name_not_empty(cls, v):
      if not v.strip():
          raise ValueError('姓名不能为空')
      return v.strip()  class UserResponse(UserBase):
      """用户响应"""
      id: int
      created_at: datetime  class Config:
      from_attributes = True  class MessageResponse(BaseModel):
      """通用响应"""
      message: str
      code: int = 0  # =====================
  # 模拟数据库
  # =====================

  users_db = []
  next_id = 1  # =====================
  # API 路由
  # =====================

  @app.get("/")
  def read_root():
      return {"message": "FastAPI + Pydantic 示例"}  @app.post("/users", response_model=UserResponse)
  def create_user(user: UserCreate):
      """创建用户"""
      global next_id  # 检查邮箱是否已存在
  if any(u["email"] == user.email for u in users_db):
      raise HTTPException(status_code=400, detail="邮箱已被注册")

  new_user = {
      "id": next_id,
      "name": user.name,
      "email": user.email,
      "age": user.age,
      "password": user.password,  # 实际应加密存储
      "created_at": datetime.now()
  }

  users_db.append(new_user)
  next_id += 1

  return new_user  @app.get("/users", response_model=List[UserResponse])
  def get_users():
      """获取所有用户"""
      return users_db  @app.get("/users/{user_id}", response_model=UserResponse)
  def get_user(user_id: int):
      """获取单个用户"""
      for user in users_db:
          if user["id"] == user_id:
              return user
      raise HTTPException(status_code=404, detail="用户不存在")  @app.delete("/users/{user_id}", response_model=MessageResponse)
  def delete_user(user_id: int):
      """删除用户"""
      global users_db  for i, user in enumerate(users_db):
      if user["id"] == user_id:
          users_db.pop(i)
          return {"message": f"用户 {user_id} 已删除", "code": 0}

  raise HTTPException(status_code=404, detail="用户不存在")  # =====================
  # 测试示例
  # =====================

  if __name__ == "__main__":
      print("=" * 50)
      print("Pydantic API 已创建!")
      print("=" * 50)
      print("\n启动方式:")
      print("  uvicorn pydantic_api:app --reload")
      print("=" * 50)



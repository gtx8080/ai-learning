# =====================
# 计算器项目
# =====================

import json
from datetime import datetime

class Calculator:
      """计算器类"""

      def __init__(self):
          self.history = []
          self.filename = "calc_history.json"

      def add(self, a, b):
          """加法"""
          result = a + b
          self._save_history("加法", a, b, result)
          return result

      def subtract(self, a, b):
          """减法"""
          result = a - b
          self._save_history("减法", a, b, result)
          return result

      def multiply(self, a, b):
          """乘法"""
          result = a * b
          self._save_history("乘法", a, b, result)
          return result

      def divide(self, a, b):
          """除法"""
          if b == 0:
              return "错误: 除数不能为0"
          result = a / b
          self._save_history("除法", a, b, result)
          return result

      def power(self, a, b):
          """幂运算"""
          result = a ** b
          self._save_history("幂运算", a, b, result)
          return result

      def _save_history(self, op, a, b, result):
          """保存历史"""
          record = {
              "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
              "operation": op,
              "a": a,
              "b": b,
              "result": result
          }
          self.history.append(record)

      def show_history(self):
          """显示历史"""
          if not self.history:
              print("没有计算历史")
              return

          print("\n=== 计算历史 ===")
          for i, record in enumerate(self.history, 1):
              print(f"{i}. [{record['time']}] {record['a']} {record['operation']} {record['b']} = {record['result']}")

      def save_to_file(self):
          """保存到文件"""
          with open(self.filename, "w", encoding="utf-8") as f:
              json.dump(self.history, f, ensure_ascii=False, indent=2)
          print(f"\n历史已保存到 {self.filename}")


# 测试
calc = Calculator()

print("=== 计算器测试 ===")
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 3 = {calc.subtract(10, 3)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"20 / 4 = {calc.divide(20, 4)}")
print(f"2 ** 10 = {calc.power(2, 10)}")
print(f"10 / 0 = {calc.divide(10, 0)}")  # 测试错误处理

calc.show_history()
calc.save_to_file()

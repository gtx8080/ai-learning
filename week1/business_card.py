# 个人名片生成器

def create_card():
	"""生成个人名片"""
	print("=" * 40)
	print("	      个人名片生成器")
	print("=" * 40)

	# 获取输入
	name = input("\n姓名: ")
	job = input("职位: ")
	company = input("公司: ")
	phone = input("电话: ")
	email = input("邮箱: ")

	#生成名片
	card = f"""
	┌{'─' * 38}┐
        │ 姓名: {name:<30} │
        │ 职位: {job:<3}  │
        │ 公司: {company:<30} │
        │ 电话: {phone:<30} │
        │ 邮箱: {email:<30} │
        └{'─' * 38}┘
        """

	print(card)

	# 保存到文件
	filename = f"{name}_card.txt"
	with open(filename, "w", encoding="utf-8") as f:
		f.write(card)
	print(f"名片已保存到: {filename}")

# 运行
create_card()

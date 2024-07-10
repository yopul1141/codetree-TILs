class info:
    def __init__(self,name = "codetree",code = 50):
        self.name = name
        self.code = code
name,code = input().split()
user_1 = info()
user_2 = info(name,code)
print(f"product {user_1.code} is {user_1.name}")
print(f"product {user_2.code} is {user_2.name}")
class info:
    def __init__(self,ID = "codetree",level = 10):
        self.ID = ID
        self.level = level
a,b = input().split()
user_1 = info()
user_2 = info(a,b)
print(f"user {user_1.ID} lv {user_1.level}")
print(f"user {user_2.ID} lv {user_2.level}")
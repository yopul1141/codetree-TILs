class info:
    def __init__(self,code,color,sec):
        self.code = code
        self.color = color
        self.sec = sec
code,color,sec = input().split()
user = info(code,color,sec)
print(f"code : {user.code}")
print(f"color : {user.color}")
print(f"second : {user.sec}")
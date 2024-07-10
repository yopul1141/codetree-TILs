class reservation:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time
code,place,time = input().split()
res = reservation(code,place,time)
print(f"secret code : {res.code}")
print(f"meeting point : {res.place}")
print(f"time : {res.time}")
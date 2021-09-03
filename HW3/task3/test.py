from datetime import datetime, timedelta


created_utc =  1630596226.0

dt = datetime.fromtimestamp(created_utc)
print(dt)

if dt >= datetime.now() - timedelta(minutes=10):
    print("!!!")

dif = (datetime.now() - dt).seconds // 3600

print(dt.strftime("%Y %m %d"))


lst = [1,2,3,4,5,6]
print(lst[-2:])
print(lst[:2])
# 装饰器:

user_info = {"tom": 123456, "jerry": 456789, "hale": 000000}

def check(i):
    def wrapper(user, password):
        if user in user_info.keys():
            if password == user_info[user]:
                i(user, password)
            else:
                print("password error")
        else:
            print("请注册")
    return wrapper

@check
def index(user, password):
    print("Welcome!!!")


index("tom", 12345)
index("jerry", 456789)

# # 调用装饰器(不推荐)
# result = check(index)
# result("tom", 123456)




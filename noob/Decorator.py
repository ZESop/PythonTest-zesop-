# def now():
#     print('2015-3-25')
#     return 1

# f = now
# print(f.__name__)

# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():'% func.__name__)
#         return func(*args,**kw)
#     return wrapper

# def yeh():
#     print(1)
# @log

# def now():
#     print('2015-3-25')

# now()

def debug(func):
    def wrapper():
        print("[DEBUG]:enter:{}()".format(func.__name__))
        return func()
    return wrapper

@debug
def say_hello():
    print ("hello!")

say_hello()
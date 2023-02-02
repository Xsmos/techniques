def foo():
    print("starting:...")
    while True:
        res = yield 4
        print("res =", res)

def foo1(num):
    print("starting...")
    while num < 10:
        num += 1
        yield num
        
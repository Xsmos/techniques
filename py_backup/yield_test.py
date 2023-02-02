def foo():
    print("starting:...")
    while True:
        res = yield 4
        print("res =", res)
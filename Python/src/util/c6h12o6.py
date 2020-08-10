def run(*args, **kwargs):
    print("C6H1O6")
    print("------")
    print("args = [")
    for a in args:
        print(a + ",")
    print("]")
    print("------")
    print("kwargs = {")
    for k, v in kwargs.items():
        print(k + ":" + v + ",")
    print("}")

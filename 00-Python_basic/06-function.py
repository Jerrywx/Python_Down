

def fun():
    abc = "哈哈"
    def fun_inner():
        print(abc)
    return fun_inner()

# print(fun())
fun()
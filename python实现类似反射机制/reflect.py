'''
python可以传类, 类也是对象, 所以天然就满足反射.
java是强类型语言, 需要产生Class类的 <类>.class / <对象>.getClass() / Class.forName("a.b.c") (包的位置) 获取类似的功能.
以下代码只是python中动态导入文件中类的方式.

'''

def run_reflect():

    getstr = input()
    module_str, fun_str = getstr.split("/")

    try:
        module = __import__(module_str)

        if hasattr(module, fun_str):
            func = getattr(module_str, fun_str)
            func()
        else:
            print(f"{module_str} / {fun_str} not exist.")

        setattr(module, "name", 5)
        print(hasattr(module, "name"))
        print(module.name)

        delattr(module, "name")

        hasattr(module, "name")
    except ImportError as e:
        print(e)
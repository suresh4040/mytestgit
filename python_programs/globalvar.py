# x = 1 #global scope
# def f():
#     x = 3 # local
#     print(x)
# f()
# print(x)


x = 1
def zz():
    x = 5
    def yy():
        global x # global will not find x in zz() func instead it will find outside of all func , if x is der it will ovverite
        x=110
    print(x)  # 5
    yy()
    print(x)  # 5
zz()
print(x)
# op
# 5
# 5
# 110
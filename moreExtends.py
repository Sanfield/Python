class Base1:
    def foo1(self):
        print("我是foo1")

class Base2:
    def foo2(self):
        print("我是foo2")
class C(Base1,Base2):
    pass

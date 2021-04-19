class A:
    def show(self):
        print("ini A")


class B(A):
    def show(self):
        print("ini B")


class C(A):
    def show(self):
        print("ini C")


class D(B,C):
    pass
    # def show(self):
    #     print("ini D")


objek = D()
objek.show()
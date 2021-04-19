class A:
    def show(self):
        print("ini A")


class B:
    def show(self):
        print("ini B")


class C(A, B):
    pass


objeck = C()
objeck.show()
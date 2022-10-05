class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return f"O valor de x é {self._x}.\n" or 0

    @x.setter
    def x(self, valor):
        self._x += valor
        print(f"O valor inserido foi {valor}.")
        print(f"Valor final: {self._x}.\n")

    @x.deleter
    def x(self):
        self._x = 0
        print("Valor deletado")


print("VALORES\n")

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)

class Passaro:
    def voar(self):
        return "Voando..."


class Pardal(Passaro):
    def voar(self):
        return super().voar()


class Avestruz(Passaro):
    def voar(self):
        return "Avestruz não voa..."

# FIXME: exemplo ruim de uso de hernaça para 'adquirir' o método voar


class Aviao(Passaro):
    def voar(self):
        return "Avião está decolando..."


def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

print(p1.voar())
print(p2.voar())
print(Aviao().voar())

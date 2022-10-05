class Veiculo:
    def __init__(self, cor, placas, nmr_rodas):
        self.nmr_rodas = nmr_rodas
        self.cor = cor
        self.placas = placas
        self.nmr_rodas = nmr_rodas

    def ligarMotor(self):
        print("Ligando o motor")


class Carro(Veiculo):
    def __init__(self, modelo, **kw):
        self.modelo = modelo
        super().__init__(**kw)


class Moto(Veiculo):
    pass


class Caminhao(Veiculo):
    pass


class AndarMixin:
    def andar(self):
        return "Andando...."


class Gol(Carro, AndarMixin):
    def __init__(self, cor, placas, nmr_rodas, modelo):
        print(Gol.__mro__)  # Mostra a sequencia da herança


motocicleta = Moto("Verde", "ABC-000", 4)
motocicleta.ligarMotor()

caminhao = Caminhao("Vermelho", "MVD-456", 4)

print("")
gol = Gol(cor="Rosa", placas="MKL-895", nmr_rodas=4, modelo="Gol")
print(gol.andar())

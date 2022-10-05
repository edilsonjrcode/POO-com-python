class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def Buzinar(self):
        print("Plim plim")

    def Parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def Correr(self):
        print("Vrummmmmmmm...")

    def __str__(self):
        return f"Bicicleta: Cor = {self.cor}, Modelo = {self.modelo}, Ano = {self.ano}, Valor = {self.modelo}"

    def nome_classe(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("Azul", "Caloi", 2022, 580)

print(f"Bicicleta {b1.modelo} {b1.cor}.\n")
print(b1)
b1.Correr()
b1.Buzinar()
b1.Parar()

print(
    f"\nA cor da bicicleta é {b1.cor}, seu modelo é {b1.modelo}, do ano de {b1.ano} e custa {b1.valor} reais.\n")

b2 = Bicicleta("Vermelha", "Monark", 2005, 430)

print(f"Bicicleta {b2.modelo} {b2.cor}.\n")
print(b2)

Bicicleta.Correr(b2)
Bicicleta.Buzinar(b2)
Bicicleta.Parar(b2)


print(
    f"\nA cor da bicicleta é {b2.cor}, seu modelo é {b2.modelo}, do ano de {b2.ano} e custa {b2.valor} reais.\n")

Bicicleta.nome_classe(b2)

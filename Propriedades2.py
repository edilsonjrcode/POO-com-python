class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return f"\nNome: {self._nome}"

    @property
    def idade(self):
        _ano_atual = 2022
        return f"Idade: {_ano_atual -self._ano_nascimento} anos"


print("PESSOAS")

pessoa = Pessoa("Giselly", 2001)
print(pessoa.nome)
print(pessoa.idade)

pessoa2 = Pessoa("Júnior", 2001)
print(pessoa2.nome)
print(pessoa2.idade)

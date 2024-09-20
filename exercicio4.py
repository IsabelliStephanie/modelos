class Pessoa:
    def __init__(self, nome='', idade='', profissão=''):
        self.nome = nome
        self.idade = idade
        self.profissão = profissão

def __str__(self):
    return f'Nome {self.nome}, Idade{self.idade}, Profissão{self.profissão}'

def aniversario(self):
    self.idade +=1

@property
def saudacao(self):
    return f'Olá, meu nome é {self.nome} e sou {self.profissao}.'

pessoa = Pessoa("Isabelli", 22, "Analista de dados")
print(pessoa) 
print(pessoa.saudacao)  

pessoa.aniversario()
print(pessoa)  

#Resumindo o código:
#Atributos: nome, idade e profissao são definidos no construtor __init__.
#Método __str__: Retorna uma representação em string da pessoa.
#Método aniversario: Aumenta a idade da pessoa em um ano.
#Propriedade saudacao: Retorna uma mensagem personalizada com base na profissão da pessoa.


#Código do professor
class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1
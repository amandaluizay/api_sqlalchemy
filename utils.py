from models import *


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=25)
    print(pessoa)
    pessoa.save()


# consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafaela').first()
    print(pessoa.idade)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafaela').first()
    pessoa.nome = 'Rafaella'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    consulta_pessoas()

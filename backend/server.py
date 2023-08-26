from flask import Flask
from datetime import datetime

app = Flask(__name__)

str_date = input('Digite o dia do banho: ')
qtdPequenos = int(input('Digite o Número de cães Pequenos: '))
qtdGrandes = int(input('Digite o Número de cães Grandes: '))


date = datetime.strptime(str_date, '%d/%m/%Y').date()


def ehFimDeSemana(date):
    if date.weekday() < 5:
        return False
    return True


def meuCaninoFeliz(qtdPequenos, qtdGrandes):
    # DISTANCIA = 2

    if ehFimDeSemana(date):
        total = (qtdPequenos * 20 + qtdGrandes * 40) * 1.2
    else:
        total = qtdPequenos * 20 + qtdGrandes * 40

    print("Total no Meu Canino Feliz: R$", total)
    return total


def vaiRex(qtdPequenos, qtdGrandes):
    # DISTANCIA = 1.7

    if ehFimDeSemana(date):
        total = qtdPequenos * 20 + qtdGrandes * 55
    else:
        total = qtdPequenos * 15 + qtdGrandes * 50

    print("Total na Vai Rex: R$", total)
    return total


def chowChawgas(qtdPequenos, qtdGrandes):
    # DISTANCIA = 0.8

    total = qtdPequenos * 30 + qtdGrandes * 45

    print("Total na ChowChawgas: R$", total)
    return total


print()

totalMeuCaninoFeliz = meuCaninoFeliz(qtdPequenos, qtdGrandes)
totalVaiRex = vaiRex(qtdPequenos, qtdGrandes)
totalChowChawgas = chowChawgas(qtdPequenos, qtdGrandes)

print()

escolha = ""

if totalChowChawgas <= totalMeuCaninoFeliz and totalChowChawgas <= totalVaiRex:
    print("Chow Chawgas foi escolhido!!!")
    escolha = "Chow Chawgas"
elif totalVaiRex <= totalMeuCaninoFeliz and totalVaiRex <= totalChowChawgas:
    print("Vai Rex foi escolhido!!!")
    escolha = "Vai Rex"
elif totalMeuCaninoFeliz <= totalVaiRex and totalMeuCaninoFeliz <= totalChowChawgas:
    print("Meu Canino Feliz foi escolhido!!!")
    escolha = "Meu Canino Feliz"


@app.route('/')
def get_time():

    return {
        'ValorMeuCaninoFeliz': totalMeuCaninoFeliz,
        "ValorVaiRex": totalVaiRex,
        "ValorChowChawgas": totalChowChawgas,
        "Escolha": escolha
    }


if __name__ == '__main__':
    app.run(debug=True)

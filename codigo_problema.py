def soma(a, b):
    return a + b

def saudacao(nome):
    print("Olá, " + nome)  # Uso de print no lugar de logger

def dividir(a, b):
    if b == 0:
        resultado = a / b  # Divisão por zero não tratada corretamente
    else:
        resultado = a / b
    return resultado

idade = "20"
if idade > 18:  # Erro semântico: comparando string com inteiro
    print("Maior de idade")

print("Isso é um log que não deveria estar em produção")  # Uso de print indevido

def nao_usada(x):
    return x * 2  # Função nunca chamada

lista = [1, 2, 3]
for i in range(5):  # Vai gerar IndexError quando i for 3 ou 4
    print(lista[i]
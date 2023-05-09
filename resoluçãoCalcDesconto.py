"""
Exercício: Calculadora de Desconto

Crie uma calculadora de desconto em Python, que solicita ao usuário que informe o valor do produto, a porcentagem de desconto e, em seguida, calcula e exibe o valor do produto com o desconto aplicado. 

P.S: Lembre-se de que o valor do desconto é obtido por meio da fórmula: valor do produto * porcentagem de desconto / 100.

Além disso, é obrigatório utilizar uma função que calcule o valor com desconto e um condicional para verificar se o valor do desconto é válido (ou seja, se o valor com desconto é menor que o valor do produto).
Ao final, exiba o resultado do desconto e informe ao usuário se o desconto informado foi válido ou não.

"""


# Resolução

def calcular_desconto(valor, porcentagem):
    desconto = valor * porcentagem / 100
    valor_com_desconto = valor - desconto
    return valor_com_desconto

valor_inicial = float(input("Insira um valor: "))
porcentagem_desconto = float(input("Insira uma porcentagem de desconto: "))

valor_com_desconto = calcular_desconto(valor_inicial, porcentagem_desconto)


if valor_com_desconto < valor_inicial:
    print(f"O valor com desconto é: R${valor_com_desconto:.2f}")
else:
    print("O desconto informado não é válido.")
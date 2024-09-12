#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# Opteir por pediro os dados para o Usuario no console 
# Como optei por pedir os dados, criei um funçao para validar o imput.
# A Validação consiste em verificar se o falor é > ou = 0 
# E validar exepiton caso o usuario digite letras

def fibonacci(n):
    anterio = 0
    atual = 1
    
    if n == anterio or n == atual:
        return f"O número {n} pertenve à sequência de Fibonacci"
    
    while atual < n:
        proximo = anterio + atual
        anterio = atual
        atual = proximo
    
    if atual == n:
        return f"O número {n} pertenve à sequência de Fibonacci"
    else:
        return f"O número {n} NÃO pertenve à sequência de Fibonacci"



def input_valido():
    while True:
        try:
             numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci "))
             if numero < 0:
                 print("Por favor, Insira um número inteiro não negativo.")
             else:
                 return numero
        except ValueError:
            print("Entrada Inválida! Por Favor, insira um número inteiro.")

numero = input_valido()
print(fibonacci(numero))
# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

numero = []
for n in range(0.6):
    digiteumnumero = int(input("digite um numero"))
    if digiteumnumero % 2 == 0:
        numero.append(digiteumnumero)

soma = sum(numero)
print(soma)
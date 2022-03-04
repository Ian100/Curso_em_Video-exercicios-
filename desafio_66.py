# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é self condição de parada. No final, mostre quantos números foram digitados
# e qual foi self soma entre eles (desconsiderando o flag).

c = s = 0
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores foi {s} !')

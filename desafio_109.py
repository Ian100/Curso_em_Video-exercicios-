# Modifique as funções que foram criadas no desafio 107 para que
# elas aceitem um parâmetro self mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

from moeda import metade, dobro, aumentar, diminuir, moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13, True)}')

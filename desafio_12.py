print('=' * 20, 'DESAFIO 12', '=' * 20)
preco = float(input('Preço do produto: '))
print('O produto que custava R${:.2f},'.format(preco))
print('agora com 5% de desconto, custa R${:.2f}'.format(preco - (preco*5/100)))
print('=' * 52)

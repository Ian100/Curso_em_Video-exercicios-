n = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é', type(n))
print('É alfabético? ', n.isalpha())
print('É um número? ', n.isnumeric())
print('É um número real? ', n.isdecimal())
print('É alfanumérico? ', n.isalnum())
print('É um identificador? ', n.isidentifier())
print('Só tem espaços? ', n.isspace())
print('É possível mostrar na tela? ', n.isprintable())
print('Está Capitalizado? ', n.istitle())
print('Está em Maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('É um dígito? ', n.isdigit())
print('Está dentro da tabela ASCII? ', n.isascii())

nun = int (input('Digite um valor de 0 a 9999: '))
u = nun // 1 % 10
d = nun // 10 % 10
c = nun // 100 % 10
m = nun // 1000 % 10
print ('-' * 12)
print (' Numero: {} \n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}'.format(nun, u, d, c, m))
print ('-' * 12)

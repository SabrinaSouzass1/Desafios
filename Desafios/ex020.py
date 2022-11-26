import random
a1 = str (input ('Aluno 01: '))
a2 = str (input ('Aluno 02: '))
a3 = str (input ('Aluno 03: '))
a4 = str (input ('Aluno 04: '))
lista = [a1,a2,a3,a4]
sorteio = random.shuffle(lista)
print ('A ordem para apresentação é {}'.format(lista))
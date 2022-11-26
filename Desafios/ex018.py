from math import radians, sin, cos, tan
angulo = float(input('Digite o Angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print (' Angulo {} \n Seno {:.2f} \n Cosseno {:.2f} \n Tangente {:.2f} '.format(angulo, seno, cosseno, tangente))
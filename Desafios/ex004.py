a = input ('Digite algo:')
print (type (a))
print ('Tem somente espaçoes: ', a.isspace())
print ('Tem somente numeros: ', a.isnumeric())
print ('Tem somente letras: ', a.isalpha())
print ('Tem alfanumerico: ', a.isalnum())
print ('Esta em maiusculas:', a.isupper())
print ('Esta em minusculas: ', a.islower())
print ('Esta capitalizada: ' , a.istitle())
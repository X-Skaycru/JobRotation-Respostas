new_string = ""
#A função input retorna sempre uma string
frase = input('Digite uma frase: ') 
print(' Você digitou: {}'.format(frase))
for palavra in frase.split(" "):
    new_string += palavra[::-1]+" "
print('\nA frase que você digitou invertida fica: {}'.format(new_string))
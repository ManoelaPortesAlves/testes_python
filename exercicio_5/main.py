new_string = ""
frase = input('Digite uma frase: ')
print(' Você digitou: {}'.format(frase))
for palavra in frase.split(" "):
    new_string += palavra[::-1]+" "
print('A frase que você digitou invertida fica: {}'.format(new_string))
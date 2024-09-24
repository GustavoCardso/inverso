
string = input('Digite o que você quer ver de trás pra frente: ')
inverso = string[::-1]
if string == '':
    print('Você não digitou nada...')
    string = input('Digite o que você quer ver de trás pra frente: ')
print(f"String original: {string}")
print(f"String invertida: {inverso}")
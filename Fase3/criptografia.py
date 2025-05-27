import sympy
from sympy import Matrix

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789, /"
CHAVE = Matrix([[3, 2], [1, 1]])

def texto_para_numeros(texto):
    texto = str(texto)
    texto = texto.upper()
    return [ALFABETO.index(c) for c in texto if c in ALFABETO] #Cria uma lista das letrar transformadas em números

def numeros_para_texto(numeros):
    return ''.join([ALFABETO[n % 39] for n in numeros]) #39 porque é o número de caracteres que tem na variável ALFABETO

def criptografar(texto):
    numeros = texto_para_numeros(texto)
    if len(numeros) % 2 != 0:
        numeros.append(ALFABETO.index('X'))
    resultado = []
    for i in range(0, len(numeros), 2):
        bloco = Matrix([[numeros[i]], [numeros[i+1]]])
        matrizCripto = CHAVE * bloco
        resultado.extend([int(x) % 39 for x in matrizCripto])
    return numeros_para_texto(resultado)

def descriptografar(texto):
    numeros = texto_para_numeros(texto)
    chaveInversa = CHAVE.inv_mod(39)
    resultado = []
    for i in range(0, len(numeros), 2):
        bloco = Matrix([[numeros[i]], [numeros[i+1]]])
        matrizDescripto = chaveInversa * bloco
        resultado.extend([int(x) % 39 for x in matrizDescripto])
    descriptografado = numeros_para_texto(resultado)
    # Remove o último caractere se for 'X', que foi colocado na função criptografar se a quantidade de letras do texto for impar
    if descriptografado.endswith("X"):
        descriptografado = descriptografado[:-1]
    try:
        return int(descriptografado)
    except:
        return descriptografado
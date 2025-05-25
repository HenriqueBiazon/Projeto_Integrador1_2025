import sympy
from sympy import Matrix

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789, /"
CHAVE = Matrix([[3, 2], [1, 1]])  # matriz simples e válida

def texto_para_numeros(texto):
    texto = str(texto)
    texto = texto.upper()
    return [ALFABETO.index(c) for c in texto if c in ALFABETO]

def numeros_para_texto(nums):
    return ''.join([ALFABETO[n % 39] for n in nums])

def criptografar(texto):
    nums = texto_para_numeros(texto)
    if len(nums) % 2 != 0:
        nums.append(ALFABETO.index('X'))
    resultado = []
    for i in range(0, len(nums), 2):
        bloco = Matrix([[nums[i]], [nums[i+1]]])
        cript = CHAVE * bloco
        resultado.extend([int(x) % 39 for x in cript])
    return numeros_para_texto(resultado)

def descriptografar(texto):
    nums = texto_para_numeros(texto)
    chave_inv = CHAVE.inv_mod(39)
    resultado = []
    for i in range(0, len(nums), 2):
        bloco = Matrix([[nums[i]], [nums[i+1]]])
        decript = chave_inv * bloco
        resultado.extend([int(x) % 39 for x in decript])
    descriptografado = numeros_para_texto(resultado)
    # Remove o último caractere se for 'X', que foi colocado na função criptografar se a quantidade de letras do texto for impar
    if descriptografado.endswith("X"):
        descriptografado = descriptografado[:-1]
    try:
        return int(descriptografado)
    except:
        return descriptografado
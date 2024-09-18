# Recebe o número inteiro do usuário
numero = input("Digite um número inteiro: ")

# Verifica se o número é um palíndromo
palindromo = True
i = 0
while i < len(numero) // 2 and palindromo:
    # Compara os caracteres da esquerda com os da direita
    if numero[i] != numero[-(i + 1)]:
        # Se forem diferentes, não é um palíndromo
        palindromo = False
    i += 1

if palindromo:
    print(numero," é um número palíndromo.")
else:
    print(numero," não é um número palíndromo.")

def somar_ate_limite(lista, limite):
    soma = 0
    indice = 0

    while soma <= limite and indice < len(lista):
        soma += lista[indice]
        indice += 1

    return soma

# Exemplo de uso
minha_lista = [1, 2, 3, 4, 5]
limite_soma = 10

resultado = somar_ate_limite(minha_lista, limite_soma)
print(f"A soma dos elementos até atingir o limite é: {resultado}")
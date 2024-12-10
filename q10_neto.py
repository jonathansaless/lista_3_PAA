def josephus(n, k):
    if n == 1: # caso base. resta uma pessoa no cículo
        return 0
    else: # Chama recursivo
        resultado = josephus(n - 1, k)
        # k = deslocamento
        # resto da divisão pela quantidade de pessoas no círculo
        return (resultado + k) % n

print("==== Problema da Lenda e Flavious Josephus ==== ")
NC = int(input("Entre com um número de casos entre 1 e 30 para testar: "))
print("n = quantidade de pessoas no cículo")
print("k = quantidade de passos entre duas pessoas no círculo")
for Z in range(NC):
    n, k = map(int, input(f"Caso {Z + 1}: Forneça os valores e n e k separados por espaço: ").split())
    resultado = josephus(n, k) + 1
    print(f"Caso {Z + 1}. Para um cículo com {n} pessoas e com {k} passos entre elas, a pessoa {resultado} restará no círculo")
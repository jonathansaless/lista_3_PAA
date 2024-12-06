import sys

# defino um novo limite de recursão para que o código funcione corretamente em valores altos de n
sys.setrecursionlimit(200000)

def josephus(n, k):
    # Caso base: se houver uma pessoa, ela será a sobrevivente
    if n == 1:
        return 0
    # Caso recorrente: calcula a posição do sobrevivente para n-1 pessoas
    else:
        return (josephus(n - 1, k) + k) % n

def main():
    NC = int(input())  # Número de casos de teste
    for case_ in range(1, NC + 1):
        primeira_linha = input()
        n, k = (int(numero) for numero in primeira_linha.split())
        
        sobrevivente = josephus(n, k) + 1
        print(f"Case {case_}: {sobrevivente}")

if __name__ == "__main__":
    main()

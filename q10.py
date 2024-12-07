import sys

# Define um novo limite de recursão para que o código funcione corretamente em valores altos de n
sys.setrecursionlimit(200000)

def josephus(n, k):
    # Caso base
    if n == 1:
        return 0
    # Caso recorrente
    else:
        return (josephus(n - 1, k) + k) % n

def main():
    NC = int(input())
    for case_ in range(1, NC + 1):
        primeira_linha = input()
        n, k = (int(numero) for numero in primeira_linha.split())
        
        sobrevivente = josephus(n, k) + 1
        print(f"Case {case_}: {sobrevivente}")

if __name__ == "__main__":
    main()

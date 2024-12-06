def josephus(n, k):
    resultado = 0  # A posição base quando n = 1 (zero-indexed)
    
    # Iteração para calcular a posição final quando n > 1
    for i in range(2, n + 1):
        resultado = (resultado + k) % i
    
    # A resposta é a posição final convertida para um índice de 1 (baseada em 1)
    return resultado + 1

def main():
    NC = int(input())  # Número de casos de teste
    for case_num in range(1, NC + 1):
        n, k = map(int, input().split())  # Leitura de n e k
        result = josephus(n, k)
        print(f"Case {case_num}: {result}")

if __name__ == "__main__":
    main()

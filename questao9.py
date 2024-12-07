def bolha(times, estatisticas):
    n = len(times)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparar os times com base nos critérios
            a, b = times[j], times[j + 1]
            if (
                (estatisticas[a]["pontos"] < estatisticas[b]["pontos"]) or
                (estatisticas[a]["pontos"] == estatisticas[b]["pontos"] and estatisticas[a]["vitorias"] < estatisticas[b]["vitorias"]) or
                (estatisticas[a]["pontos"] == estatisticas[b]["pontos"] and estatisticas[a]["vitorias"] == estatisticas[b]["vitorias"] and estatisticas[a]["gols"] < estatisticas[b]["gols"]) or
                (estatisticas[a]["pontos"] == estatisticas[b]["pontos"] and estatisticas[a]["vitorias"] == estatisticas[b]["vitorias"] and estatisticas[a]["gols"] == estatisticas[b]["gols"] and estatisticas[a]["colocacao"] > estatisticas[b]["colocacao"])
            ):
                # Trocar os times de lugar
                temp = times[j]
                times[j] = times[j + 1]
                times[j + 1] =  temp


def verifica_entrada(prompt, value_type=int, min_val=None, max_val=None):
    """Utility to get a valid input with type and range checks."""
    while True:
        try:
            value = value_type(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"O valor deve estar entre {min_val} e {max_val}. Tente novamente.")
            else:
                return value
        except ValueError:
            print(f"Valor inválido. Entre com um valor numérico inteiro {value_type.__name__}.")

def classificacao():
    T = verifica_entrada("Forneça um valor de casos de teste entre 1 e 100: ", int, 1, 100)
    resultados = []
    
    for t in range(T):
        print(f"\nCaso de Teste {t + 1}")
        
        # Entra com o número de times e partidas
        N = verifica_entrada("Entre com a quantidade de times entre 2 e 100: ", int, 2, 100)
        M = verifica_entrada("Entre com a quantidade de partidas entre 1 e 1000: ", int, 1, 1000)


        # Entra com o nome dos times
        print(" ==== Entre com o nome dos Times: ====")
        times = []
        for i in range(N):
            while True:
                nome_time = input(f"Time {i + 1}: ").strip()
                if nome_time.isalpha() and 1 <= len(nome_time) <= 20:
                    times.append(nome_time)
                    break
                else:
                    print("O nome do time deve ter no máximo 20 caracteres sem números. Tente novamente.")

        #print(times)
        # Inicializa o quadro de classificação dos times
        estatisticas = {}
        for colocacao, iterador in enumerate(times):
            estatisticas[iterador] = {
               "pontos": 0,
               "vitorias": 0,
               "gols": 0,
               "colocacao": colocacao
            }

        # Coletar o resultado das partidas
        for Z in range(M):
            print(f"Entre com o resultado da partida {Z + 1} no formato '0 timeA 1 timeB'):")
            while True:
                try:
                    partida = input().split()
                    if len(partida) != 4:
                        raise ValueError("Formato inválido. Forneça entrada no formato '1 timeA 0 timeB'.")
                    X, timeA, Y, timeB = int(partida[0]), partida[1], int(partida[2]), partida[3]
                    if X < 0 or X > 100 or Y < 0 or Y > 100:
                        raise ValueError("Gols devem estar entre 0 e 100.")
                    if timeA not in times or timeB not in times or timeA == timeB:
                        raise ValueError("Nome do time inválido ou partida com o mesmo time.")
                    break
                except ValueError as e:
                    print(e, "Tente novamente.")

            # Atualiza quantidade de gols
            estatisticas[timeA]["gols"] += X
            estatisticas[timeB]["gols"] += Y

            # Atualiza pontos e vitorias
            if X > Y:  # vitoria do timeA
                estatisticas[timeA]["pontos"] += 3
                estatisticas[timeA]["vitorias"] += 1
            elif X < Y:  # vitoria do timeB
                estatisticas[timeB]["pontos"] += 3
                estatisticas[timeB]["vitorias"] += 1
            else:  # empate
                estatisticas[timeA]["pontos"] += 1
                estatisticas[timeB]["pontos"] += 1
            
    # Ordena os times conforme classificação
    bolha(times, estatisticas)

    # Imprimir os times em ordem de classificação conforme critérios
    print("Resultados:")
    for time in times:
        print(f"{time}: Pontos: {estatisticas[time]["pontos"]} Vitorias: {estatisticas[time]["vitorias"]} Gols: {estatisticas[time]["gols"]}")


# Run the function
if __name__ == "__main__":
    classificacao()

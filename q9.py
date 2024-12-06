class Tabela():
    def __init__(self, times):
        self.times = times

    def atualiza(self, jogo):
        golsX, timeA, golsY, timeB = jogo

        golsA = int(golsX)
        golsB = int(golsY)

        # Verificação de número de gols válidos
        if not (0 <= golsA <= 100) or not (0 <= golsB <= 100):
            print('Número de gols inválido. O número de gols deve ser entre 0 e 100.')
            return

        timeA_obj = None
        timeB_obj = None
        
        for time in self.times:
            if time.nome == timeA:
                timeA_obj = time
            if time.nome == timeB:
                timeB_obj = time

        if timeA_obj and timeB_obj:

            timeA_obj.gols += golsA
            timeB_obj.gols += golsB

            if golsA > golsB:  # TimeA vence
                timeA_obj.pontos += 3
                timeA_obj.vitorias += 1
            elif golsA < golsB:  # TimeB vence
                timeB_obj.pontos += 3
                timeB_obj.vitorias += 1
            else:  # Empate
                timeA_obj.pontos += 1
                timeB_obj.pontos += 1
        else:
            print(f"Um ou ambos os times não foram encontrados na lista de times.")

    def classificacao(self):
        # Ordenar os times pela quantidade de pontos, vitórias e gols
        self.times.sort(key=self._criterios_classificacao)
        return self.times

    def _criterios_classificacao(self, time):
        # 1. Pontos (decrescente)
        # 2. Vitórias (decrescente)
        # 3. Gols (decrescente)
        return (-time.pontos, -time.vitorias, -time.gols)

class Time():
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.gols = 0

def main():
    # T = Número de casos de teste
    T = int(input())

    for _ in range(T):
        primeira_linha = input()
        # N = Número de times
        # M = Número de jogos
        N, M = (int(numero) for numero in primeira_linha.split())

        # Verificação dos limites de N e M
        if not (2 <= N <= 100):
            print("Número de times inválido. O número de times deve ser entre 2 e 100.")
            continue
        if not (1 <= M <= 1000):
            print("Número de jogos inválido. O número de jogos deve ser entre 1 e 1000.")
            continue

        # Criação dos times
        times = []
        for i in range(N):
            time = input().strip()
            times.append(Time(time))

        tabela = Tabela(times)
        
        # Recebendo os jogos
        for _ in range(M):
            jogo = input().split()
            tabela.atualiza(jogo)

        # Classificação final
        classificados = tabela.classificacao()
        
        # Exibindo a classificação para o caso atual
        for time in classificados:
            print(time.nome)

if __name__=='__main__':
    main()

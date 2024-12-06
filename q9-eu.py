# Questão 09
class Tabela():
    def __init__(self, times):
        self.times = times
        self.classificacao_times = {}

    def atualiza(self, jogo):
        golsX, timeA, golsY, timeB = jogo

        golsA = int(golsX)
        golsB = int(golsY)

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

    while True:
        primeira_linha = input()
        # N = Número de times
        # M = Número de jogos
        N, M = (int(numero) for numero in primeira_linha.split())
        if N < 2 or N > 100:
            print('Número de times inválido. O número de times deve ser entre 2 e 100.')
        elif M < 1 or M > 1000:
            print('Número de jogos inválido. O número de jogos deve ser entre 1 e 1000.')
        else:
            break

    for _ in range(T):
        times = []
        i = 0
        while i < N:
            # Recebe o nome da equipe
            time = input().strip()
            # verifica se o time digitado já está na lista de times
            if time in times:
                print('O time já existe, digite um novo nome!')
            else:
                times.append(Time(time))
                i+=1
        tabela = Tabela(times)
        i = 0
        while i < M:
            # Recebe o resultado do jogo
            jogo = input().split()
            # verifica se quantidade de gols é válida
            if not (0 <= int(jogo[0]) <= 100) or not (0 <= int(jogo[2]) <= 100):
                print('Número de gols inválido. O número de gols deve ser entre 0 e 100.')
            else:
                tabela.atualiza(jogo)
                i+=1

         # Classificação final
        classificados = tabela.classificacao()
        
        # Exibindo a classificação para o caso atual
        for time in classificados:
            print(time.nome)

if __name__=='__main__':
    main()
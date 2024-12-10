# Cria um objeto Tabela que possui uma lista de objetos de Time
class Tabela():
    def __init__(self, times):
        self.times = times

    def atualiza(self, jogo):
        golsX, timeA, golsY, timeB = jogo

        golsA = int(golsX)
        golsB = int(golsY)

        # Verificação de número de gols válidos (0 a 100 gols)
        if not (0 <= golsA <= 100) or not (0 <= golsB <= 100):
            print('Número de gols inválido. O número de gols deve ser entre 0 e 100.')
            return

        timeA_obj = None
        timeB_obj = None
        
        # Verifica se os nomes dos times do jogo estão presentes no campeonato, se sim recebe os objetos que foram criados para cada time
        for time in self.times:
            if time.nome == timeA:
                timeA_obj = time
            if time.nome == timeB:
                timeB_obj = time

        # Se os nomes dos times do jogo estão no campeonato, prossegue na atualização da tabela
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
        # Ordenar os times pela quantidade de pontos, vitórias e gols usando Merge Sort (complexidade nlogn)
        self.times = self.merge_sort(self.times)
        return self.times

    def merge_sort(self, times):
        if len(times) <= 1:
            return times

        # Divisão inteira //
        meio = len(times) // 2
        esquerda = self.merge_sort(times[:meio])
        direita = self.merge_sort(times[meio:])

        return self.merge(esquerda, direita)

    def merge(self, esquerda, direita):
        lista_ordenada = []
        i = 0
        j = 0

        while i < len(esquerda) and j < len(direita):
            # Comparação usando os critérios de classificação
            if self._criterios_classificacao(esquerda[i]) <= self._criterios_classificacao(direita[j]):
                lista_ordenada.append(esquerda[i])
                i += 1
            else:
                lista_ordenada.append(direita[j])
                j += 1

        # Adiciona os elementos restantes
        lista_ordenada.extend(esquerda[i:])
        lista_ordenada.extend(direita[j:])
        return lista_ordenada

    def _criterios_classificacao(self, time):
        # 1. Pontos (decrescente)
        # 2. Vitórias (decrescente)
        # 3. Gols (decrescente)
        return (-time.pontos, -time.vitorias, -time.gols)

# Cria um objeto de Time que possui um nome, pontos, número de vitórias e número de gols
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

        times = []
        i = 0

        # Recebendo os times
        while i < N:
            time = input().strip()
            # Verifica se time já existe
            if time in times:
                print('O time já existe, digite um novo nome!')
            else:
                times.append(Time(time))
                i+=1

        tabela = Tabela(times)
        
        # Recebendo os jogos
        for _ in range(M):
            jogo = input().split()
            tabela.atualiza(jogo)

        # Organiza a classificação final e recebe a lista de times em orderm de classificação
        classificacao_ordenada = tabela.classificacao()
        
        # Printa os nomes dos times em ordem de classificação
        for time in classificacao_ordenada:
            print(time.nome)

if __name__=='__main__':
    main()

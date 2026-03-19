# Essa versão do Jogo da velha ainda necessita de dois jogadores para funcionar
# Para acessar uma versão com IA integrada entre na brancj minimax

# Define a classe principal que gerencia o jogo da velha
class JogoVelha:
    # Método construtor que inicializa o jogo
    def __init__(self):
        # Cria um tabuleiro 3x3 preenchido com espaços em branco (posições vazias)
        # Usa list comprehension para criar uma matriz bidimensional
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        
        # Solicita o nome do Jogador 1 e atribui o marcador "X"
        self.jogador1, self.marcador1 = input("Nome do Jogador 1 (X): "), "X"
        
        # Solicita o nome do Jogador 2 e atribui o marcador "O"
        self.jogador2, self.marcador2 = input("Nome do Jogador 2 (O): "), "O"

    # Método que marca uma posição no tabuleiro se estiver vazia
    def marcar_tabuleiro(self, linha, coluna, marcador):
        # Verifica se a posição [linha][coluna] está vazia
        if self.tabuleiro[linha][coluna] == " ":
            # Se vazia, marca com o marcador do jogador atual (X ou O)
            self.tabuleiro[linha][coluna] = marcador
            # Retorna True indicando que a marcação foi bem-sucedida
            return True
        # Se a posição já está ocupada, retorna False
        return False

    # Método que verifica se há um vencedor no jogo
    def check_winner(self):
        # Loop que verifica linhas e colunas (índice i de 0 a 2)
        for i in range(3):
            # Verifica se os 3 elementos da linha i são iguais e não estão vazios
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != ' ':
                # Se há 3 marcadores iguais na linha, há um vencedor
                return True
            
            # Verifica se os 3 elementos da coluna i são iguais e não estão vazios
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != ' ':
                # Se há 3 marcadores iguais na coluna, há um vencedor
                return True
            
            # Verifica a diagonal principal (0,0 até 2,2)
            if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
                # Se há 3 marcadores iguais na diagonal, há um vencedor
                return True
            
            # Verifica a diagonal secundária (0,2 até 2,0)
            if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
                # Se há 3 marcadores iguais na diagonal, há um vencedor
                return True

            # Se nenhuma combinação vencedora foi encontrada nesta iteração
            return False

    # Método que exibe o tabuleiro formatado no console
    def mostrar_tabuleiro(self):
        # Imprime uma linha em branco para melhor visualização
        print("\n")
        # Inicializa o contador de linhas exibidas
        count = 0
        # Itera sobre cada linha (lista) do tabuleiro
        for row in self.tabuleiro:
            # Junta os elementos da linha com "|" como separador
            print("|".join(row))
            # Incrementa o contador
            count +=1
            # Se não foi a última linha, exibe um separador visual
            if count < 3:
                print("-" * 5)

        # Imprime uma linha em branco ao final
        print("\n")


    # Método principal que controla o fluxo do jogo
    def jogada(self, turno_atual=0):
        # Loop infinito que continua até haver um vencedor ou empate
        while True:
            # Exibe o número do turno atual
            print(f"Turno Atual: {turno_atual}")
            # Exibe o tabuleiro formatado
            self.mostrar_tabuleiro()
            
            # Determina qual jogador está na vez baseado no número do turno (par ou ímpar)
            if turno_atual % 2 == 0:
                # Se o turno é par (0, 2, 4...), é a vez do Jogador 1
                jogador_atual, marcador_atual = self.jogador1, self.marcador1
            else:
                # Se o turno é ímpar (1, 3, 5...), é a vez do Jogador 2
                jogador_atual, marcador_atual = self.jogador2, self.marcador2
            
            # Exibe qual jogador tem a vez de jogar
            print(f"Vez de {jogador_atual} ({marcador_atual})")

            # Bloco try-except para capturar erros de entrada
            try:
                # Solicita entrada do jogador e converte para inteiros
                linha, coluna = map(int, input("Escolha a linha e a coluna (0, 1, 2): ").split())

            # Captura erros de conversão ou acesso a índice inválido
            except (ValueError, IndexError):
                # Exibe mensagem de erro
                print("Entrada inválida. Use somente os números 0, 1 ou 2 para linha ou coluna")
                print("Tente novamente")
                # Chama recursivamente a função para nova tentativa
                self.jogada(turno_atual)

            # Tenta marcar a posição escolhida
            if self.marcar_tabuleiro(linha, coluna, marcador_atual):
                # Se a marcação foi bem-sucedida, verifica se há vencedor
                if self.check_winner():
                    # Exibe o tabuleiro final
                    self.mostrar_tabuleiro()
                    # Anuncia o vencedor
                    print(f"Parabéns {jogador_atual}, você venceu!")
                    # Sai do loop (fim do jogo)
                    break
                # Incrementa o turno para o próximo jogador
                turno_atual += 1
                # Verifica se o tabuleiro está completamente preenchido (9 turnos = 9 posições)
                if turno_atual == 9:
                    # Exibe o tabuleiro final
                    self.mostrar_tabuleiro()
                    # Anuncia empate
                    print("Empate!")
                    # Sai do loop (fim do jogo)
                    break
            else:
                # Se a marcação falhou (posição já ocupada), avisa o jogador
                print("Jogada inválida. Tente novamente.")
            
# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Cria uma instância da classe JogoVelha
    jogo = JogoVelha()
    # Imprime linhas em branco para melhor visualização
    print()         
    # Exibe mensagem de boas-vindas
    print("Bem-vindo ao Jogo da Velha!")
    # Exibe os nomes dos jogadores e seus marcadores
    print(f"{jogo.jogador1} (X) vs {jogo.jogador2} (O)")
    # Imprime linha em branco
    print()
    # Inicia o jogo chamando o método jogada
    jogo.jogada() 

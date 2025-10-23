import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong - 2 Jogadores")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Configurações do jogo
FPS = 60
VELOCIDADE_RAQUETE = 7
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5

# Classe da Raquete
class Raquete:
    def __init__(self, x, y):
        self.largura = 15
        self.altura = 100
        self.x = x
        self.y = y
        self.velocidade = VELOCIDADE_RAQUETE
        self.pontos = 0
    
    def desenhar(self):
        pygame.draw.rect(TELA, BRANCO, (self.x, self.y, self.largura, self.altura))
    
    def mover_cima(self):
        if self.y > 0:
            self.y -= self.velocidade
    
    def mover_baixo(self):
        if self.y < ALTURA - self.altura:
            self.y += self.velocidade
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

# Classe da Bola
class Bola:
    def __init__(self):
        self.tamanho = 15
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        # velocidade base mantida para reset
        self.base_vel_x = VELOCIDADE_BOLA_X
        self.base_vel_y = VELOCIDADE_BOLA_Y
        self.vel_x = self.base_vel_x
        self.vel_y = self.base_vel_y
        # multiplicador que aumenta a cada batida na raquete
        self.speed_multiplier = 1.0
    
    def desenhar(self):
        pygame.draw.circle(TELA, BRANCO, (self.x, self.y), self.tamanho)
    
    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Colisão com topo e fundo
        if self.y <= self.tamanho or self.y >= ALTURA - self.tamanho:
            self.vel_y *= -1
    
    def resetar(self, direcao):
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        # resetar velocidades e multiplicador ao marcar ponto
        self.speed_multiplier = 1.0
        self.vel_x = self.base_vel_x * direcao
        self.vel_y = self.base_vel_y
    
    def get_rect(self):
        return pygame.Rect(self.x - self.tamanho, self.y - self.tamanho, 
                          self.tamanho * 2, self.tamanho * 2)

# Função para desenhar linha central
def desenhar_linha_central():
    for i in range(0, ALTURA, 20):
        pygame.draw.rect(TELA, BRANCO, (LARGURA // 2 - 2, i, 4, 10))

# Função para desenhar placar
def desenhar_placar(pontos_esquerda, pontos_direita):
    fonte = pygame.font.Font(None, 74)
    texto_esquerda = fonte.render(str(pontos_esquerda), True, BRANCO)
    texto_direita = fonte.render(str(pontos_direita), True, BRANCO)
    TELA.blit(texto_esquerda, (LARGURA // 4, 50))
    TELA.blit(texto_direita, (3 * LARGURA // 4 - 37, 50))


def desenhar_menu():
    TELA.fill(PRETO)
    titulo_fonte = pygame.font.Font(None, 96)
    botao_fonte = pygame.font.Font(None, 48)

    titulo = titulo_fonte.render("PONG", True, BRANCO)
    titulo_rect = titulo.get_rect(center=(LARGURA // 2, ALTURA // 3))
    TELA.blit(titulo, titulo_rect)

    # Botão Play
    botao_w, botao_h = 240, 72
    botao_rect = pygame.Rect(0, 0, botao_w, botao_h)
    botao_rect.center = (LARGURA // 2, ALTURA // 2)
    pygame.draw.rect(TELA, BRANCO, botao_rect, border_radius=8)
    texto_play = botao_fonte.render("PLAY", True, PRETO)
    texto_rect = texto_play.get_rect(center=botao_rect.center)
    TELA.blit(texto_play, texto_rect)

    instrucoes = pygame.font.Font(None, 28).render("W/S = Jogador Esquerdo  |  ↑/↓ = Jogador Direito", True, BRANCO)
    instr_rect = instrucoes.get_rect(center=(LARGURA // 2, ALTURA // 2 + 80))
    TELA.blit(instrucoes, instr_rect)

    pygame.display.flip()
    return botao_rect

# Função para exibir mensagem de vitória
def exibir_vencedor(vencedor):
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render(f"Jogador {vencedor} Venceu!", True, BRANCO)
    texto_rect = texto.get_rect(center=(LARGURA // 2, ALTURA // 2))
    TELA.blit(texto, texto_rect)
    
    fonte_pequena = pygame.font.Font(None, 36)
    texto_reiniciar = fonte_pequena.render("Pressione ESPAÇO para jogar novamente", True, BRANCO)
    texto_rect2 = texto_reiniciar.get_rect(center=(LARGURA // 2, ALTURA // 2 + 60))
    TELA.blit(texto_reiniciar, texto_rect2)

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    
    # Criação dos objetos
    raquete_esquerda = Raquete(30, ALTURA // 2 - 50)
    raquete_direita = Raquete(LARGURA - 45, ALTURA // 2 - 50)
    bola = Bola()
    
    # Começa no menu. Ao pressionar Play ou tecla (espaço/enter) o jogo começa.
    jogo_ativo = False
    game_state = 'menu'  # 'menu', 'playing'
    vencedor = None
    PONTOS_VITORIA = 5
    
    # Loop principal
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_state == 'menu':
                # tratar clique no botão Play ou teclas para iniciar
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mouse_pos = evento.pos
                    # verificar clique no botão (precisamos obter o rect desenhado)
                    # -> desenhar_menu retorna o rect, mas aqui apenas checamos após desenhar abaixo
                    # vamos capturar no fluxo principal
                if evento.type == pygame.KEYDOWN:
                    if evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                        # iniciar jogo
                        game_state = 'playing'
                        jogo_ativo = True
                        vencedor = None
                        raquete_esquerda.pontos = 0
                        raquete_direita.pontos = 0
                        bola.resetar(1)

            else:
                # Durante o jogo ou quando mostrar vencedor, permitir reiniciar com SPACE
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE and vencedor:
                        # Reiniciar jogo
                        raquete_esquerda.pontos = 0
                        raquete_direita.pontos = 0
                        bola.resetar(1)
                        vencedor = None
                        jogo_ativo = True
        
        if game_state == 'menu':
            # desenhar menu e capturar clique no botão Play
            botao_rect = desenhar_menu()
            # processar clique no botão de iniciar (checar eventos recentes)
            # simples verificação de evento de clique usando pygame.mouse.get_pressed
            if pygame.mouse.get_pressed()[0]:
                if botao_rect.collidepoint(pygame.mouse.get_pos()):
                    game_state = 'playing'
                    jogo_ativo = True
                    vencedor = None
                    raquete_esquerda.pontos = 0
                    raquete_direita.pontos = 0
                    bola.resetar(1)
                    # pequena espera até soltar o botão para evitar múltiplos clicks
                    pygame.time.wait(150)
            # pequeno delay para reduzir uso CPU enquanto no menu
            clock.tick(FPS)
            continue

        if jogo_ativo:
            # Controles
            teclas = pygame.key.get_pressed()
            
            # Jogador 1 (Esquerda) - W e S
            if teclas[pygame.K_w]:
                raquete_esquerda.mover_cima()
            if teclas[pygame.K_s]:
                raquete_esquerda.mover_baixo()
            
            # Jogador 2 (Direita) - Setas
            if teclas[pygame.K_UP]:
                raquete_direita.mover_cima()
            if teclas[pygame.K_DOWN]:
                raquete_direita.mover_baixo()
            
            # Movimento da bola
            bola.mover()
            
            # Colisão com raquetes
            if bola.get_rect().colliderect(raquete_esquerda.get_rect()):
                if bola.vel_x < 0:
                    # inverte a direção e aumenta a velocidade pela multiplicador
                    bola.vel_x *= -1
                    bola.speed_multiplier *= 1.1
                    bola.vel_x = int(bola.vel_x * bola.speed_multiplier / 1.1)
                    bola.vel_y = bola.vel_y * bola.speed_multiplier
                    # Adiciona efeito baseado na posição de colisão
                    diferenca = (bola.y - (raquete_esquerda.y + raquete_esquerda.altura // 2))
                    bola.vel_y = diferenca * 0.1
            
            if bola.get_rect().colliderect(raquete_direita.get_rect()):
                if bola.vel_x > 0:
                    bola.vel_x *= -1
                    bola.speed_multiplier *= 1.1
                    bola.vel_x = int(bola.vel_x * bola.speed_multiplier / 1.1)
                    bola.vel_y = bola.vel_y * bola.speed_multiplier
                    diferenca = (bola.y - (raquete_direita.y + raquete_direita.altura // 2))
                    bola.vel_y = diferenca * 0.1
            
            # Pontuação
            if bola.x <= 0:
                raquete_direita.pontos += 1
                bola.resetar(1)
                if raquete_direita.pontos >= PONTOS_VITORIA:
                    jogo_ativo = False
                    vencedor = 2
            
            if bola.x >= LARGURA:
                raquete_esquerda.pontos += 1
                bola.resetar(-1)
                if raquete_esquerda.pontos >= PONTOS_VITORIA:
                    jogo_ativo = False
                    vencedor = 1
        
        # Desenhar tudo
        TELA.fill(PRETO)
        desenhar_linha_central()
        desenhar_placar(raquete_esquerda.pontos, raquete_direita.pontos)
        raquete_esquerda.desenhar()
        raquete_direita.desenhar()
        bola.desenhar()
        
        if vencedor:
            exibir_vencedor(vencedor)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
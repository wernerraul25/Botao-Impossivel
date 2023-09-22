import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições de tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hoje Tem?")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Posição inicial do botão "Não"
non_x, non_y = WIDTH // 2, HEIGHT // 2

# Fonte
font = pygame.font.Font(None, 36)

# Função para desenhar os botões
def desenhar_botoes():
    screen.fill(WHITE)
    pygame.draw.rect(screen, (0, 255, 0), (100, 250, 100, 50))  # Botão "Sim"
    pygame.draw.rect(screen, (255, 0, 0), (non_x, non_y, 100, 50))  # Botão "Não"
    
    # Texto nos botões
    sim_text = font.render("Sim", True, BLACK)
    nao_text = font.render("Não", True, BLACK)
    screen.blit(sim_text, (125, 265))
    screen.blit(nao_text, (non_x + 25, non_y + 15))

# Função para desenhar o título
def desenhar_titulo():
    titulo_text = font.render("Cuzinho hoje?", True, BLACK)
    screen.blit(titulo_text, (WIDTH // 2 - titulo_text.get_width() // 2, 50))

# Loop principal
imagem_mostrada = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 100 <= x <= 200 and 250 <= y <= 300:
                # Quando o botão "Sim" é clicado, exibir a imagem em tela cheia
                imagem = pygame.image.load('imagem_comemorando.jpeg')
                imagem = pygame.transform.scale(imagem, (WIDTH, HEIGHT))  # Redimensiona a imagem para a tela inteira
                screen.blit(imagem, (0, 0))
                pygame.display.flip()
                imagem_mostrada = True
            elif non_x <= x <= non_x + 100 and non_y <= y <= non_y + 50:
                non_x = random.randint(0, WIDTH - 100)
                non_y = random.randint(0, HEIGHT - 50)
                imagem_mostrada = False

    if not imagem_mostrada:
        desenhar_botoes()
        desenhar_titulo()
        pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
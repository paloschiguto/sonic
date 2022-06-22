import pygame, random
pygame.init()
largura = 960
altura = 672
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Sonic")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("imagens/ícone.ico")
pygameDisplay.set_icon(gameIcon)
bg = pygame.image.load("imagens/background.png")
bg_destroy = pygame.image.load("imagens/backgroundD.png")
somMorte = pygame.mixer.Sound("sounds/purr.wav")
somMorte.set_volume(0.5)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event
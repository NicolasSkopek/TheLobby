import pygame
import sys

from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import WIDTH, HEIGHT


class EndGame(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Obj("assets/menu/endgame.png", [0, 0], self.all_sprites)

        self.music = pygame.mixer.Sound("assets/sounds/endgame.mp3")
        self.music.play(-1)

        self.btn_return = Button(1050, 380, "return to menu", self.next_scene)
        self.btn_quit = Button(1050, 430, "quit", self.quit_game)

        # Lista de imagens para o efeito de transição
        self.images = [
            pygame.image.load("assets/menu/image1.png"),
            pygame.image.load("assets/menu/image2.png"),
            pygame.image.load("assets/menu/image3.png"),
            pygame.image.load("assets/menu/image4.png")
        ]
        self.current_image_index = 0  # Índice da imagem atual
        self.alpha = 0  # Transparência inicial (0 = totalmente transparente)
        self.fade_in = True  # Controla se o fade é para entrada ou saída

        self.image_display_time = 6000  # Tempo para exibir cada imagem em milissegundos
        self.fade_out_delay = 3000  # Tempo em milissegundos para aguardar antes de iniciar o fade-out
        self.last_change_time = pygame.time.get_ticks()  # Armazena o tempo da última troca de imagem
        self.fade_out_start_time = None  # Marca o tempo de início do fade-out

    def next_scene(self):
        self.music.stop()
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def events(self, event):
        self.btn_return.events(event)
        self.btn_quit.events(event)

        return super().events(event)

    def update(self):

        # Verifica o tempo de transição de imagem
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change_time > self.image_display_time:
            self.last_change_time = current_time
            self.current_image_index = (self.current_image_index + 1) % len(self.images)

            # Inicia o fade-in da nova imagem
            self.alpha = 0
            self.fade_in = True
            self.fade_out_start_time = None  # Reseta o tempo do fade-out

        # Gerenciamento do fade-in/fade-out
        if self.fade_in:
            self.alpha += 5  # Aumenta a opacidade
            if self.alpha >= 255:
                self.alpha = 255
                self.fade_in = False  # Muda para fade-out quando atingir opacidade total
                self.fade_out_start_time = current_time  # Marca o início do fade-out
        else:
            # Verifica se o tempo de delay para iniciar o fade-out já passou
            if self.fade_out_start_time and current_time - self.fade_out_start_time >= self.fade_out_delay:
                self.alpha -= 2  # Diminui a opacidade mais lentamente
            if self.alpha <= 0:
                self.alpha = 0
                self.fade_in = True  # Muda para fade-in quando atingir total transparência

        # Cria uma cópia da imagem atual com a transparência aplicada
        image = self.images[self.current_image_index].copy()
        image.set_alpha(self.alpha)

        # Desenha a imagem com o efeito de fade
        self.window.blit(image, (300, 300))  # Exibe a imagem com fade

        # Desenha os botões
        self.btn_return.draw()
        self.btn_quit.draw()

        # Atualiza a tela
        pygame.display.flip()

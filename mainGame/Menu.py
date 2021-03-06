import os

import pygame
from mainGame import Model as train
from mainGame import BestModel as best
from mainGame import Checkpoint as checkpoint
from mainGame import ManualGame as manual

# window size
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
pygame.display.set_caption('BIAI FlappyGame')


class Logo(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Background(pygame.sprite.Sprite):
    def __init__(self, image_name, location):
        # call pygame Sprite initializer
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# Button class
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.Font("../assets/fonts/FlappyBirdy.ttf", 50)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


def redrawWindow(train_button, best_button, end_button, checkpoint_button, manual_button):
    train_button.draw(screen, (0, 0, 0))
    best_button.draw(screen, (0, 0, 0))
    end_button.draw(screen, (0, 0, 0))
    checkpoint_button.draw(screen, (0, 0, 0))
    manual_button.draw(screen, (0, 0, 0))


def quitGame():
    pygame.quit()
    quit()


def main():
    run = True
    checkpoint_button = Button((0, 255, 0), 175, 100, 150, 50, "Checkpoint")
    train_button = Button((0, 255, 0), 175, 170, 150, 50, "Train")
    best_button = Button((0, 255, 0), 175, 240, 150, 50, "Best")
    manual_button = Button((0, 255, 0), 175, 310, 150, 50, "Manual")
    end_button = Button((0, 255, 0), 175, 380, 150, 50, "Quit")
    background = Background("../assets/sprites/background-blue.png", [0, 0])
    logo = Logo("../assets/sprites/flappy_bird_logov1.png", [125, 10])
    while run:
        screen.fill([1, 1, 155])
        screen.blit(background.image, background.rect)
        screen.blit(logo.image, logo.rect)
        redrawWindow(train_button, best_button, end_button, checkpoint_button, manual_button)
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if train_button.isOver(pos):
                    train.main()

                if best_button.isOver(pos):
                    best.main()

                if manual_button.isOver(pos):
                    manual.main()

                if end_button.isOver(pos):
                    run = False
                    quitGame()

                if checkpoint_button.isOver(pos):
                    checkpoint.main()

            if event.type == pygame.MOUSEMOTION:
                if train_button.isOver(pos):
                    train_button.color = (255, 0, 0)
                else:
                    train_button.color = (255, 255, 255)

                if best_button.isOver(pos):
                    best_button.color = (255, 0, 0)
                else:
                    best_button.color = (255, 255, 255)

                if end_button.isOver(pos):
                    end_button.color = (255, 0, 0)
                else:
                    end_button.color = (255, 255, 255)

                if checkpoint_button.isOver(pos):
                    checkpoint_button.color = (255, 0, 0)
                else:
                    checkpoint_button.color = (255, 255, 255)

                if manual_button.isOver(pos):
                    manual_button.color = (255, 0, 0)
                else:
                    manual_button.color = (255, 255, 255)


if __name__ == "__main__":
    main()

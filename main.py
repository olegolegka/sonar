import pygame
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Моя игра")
window.fill("blue")
image = pygame.image.load(r"C:\Users\User\Downloads\image(2).png")
rect = image.get_rect(center = (250,250))
window.blit(image,rect)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

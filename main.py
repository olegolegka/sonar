import pygame
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Моя игра")
window.fill("blue")

tnr = pygame.font.SysFont("Times New Roman",50)

message = tnr.render("Привет, Олег",1,"red","yellow")
window.blit(message,(20,20))
hel = pygame.font.SysFont("Helvetica",50)

message = hel.render("Привет, Олег",1,"red","yellow")
window.blit(message,(20,80))
arial = pygame.font.SysFont("Arial",50)

message = arial.render("Привет, Олег",1,"red","yellow")
window.blit(message,(20,130))
calibri = pygame.font.SysFont("Calibri",50)

message = calibri.render("Привет, Олег",1,"red","yellow")
window.blit(message,(20,180))
# pygame.draw.line(window,"white",[0,500],[500,0],2)
# pygame.draw.rect(window,"white",[100,80,50,20])
# pygame.draw.circle(window,"white",[400,400],50)
# pygame.draw.polygon(window,"white",[[50,30],[100,20],[120,50],[180,30],[50,50]])
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

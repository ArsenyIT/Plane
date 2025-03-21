import pygame
pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.mouse.set_visible(False)
pygame.display.set_caption("Самолёты")
background_image = pygame.image.load('resours/Небо.png').convert()

plane1_image = pygame.image.load('resours/Самолёт3.png').convert()
plane1_image = pygame.transform.flip(plane1_image, True, False)
plane1_image.set_colorkey((255, 255, 255))
plane1_rect = plane1_image.get_rect()

plane2_image = pygame.image.load('resours/Самолёт4.png').convert()
plane2_rect = plane2_image.get_rect()
plane2_image.set_colorkey((255, 255, 255))

FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, [0, 0])

    mouse_position = pygame.mouse.get_pos()
    plane2_rect.x = mouse_position[0]
    plane2_rect.y = mouse_position[1]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane1_rect.left > 5:
        plane1_rect.x -= 5
    elif keys[pygame.K_RIGHT] and plane1_rect.right < screen_width - 5:
        plane1_rect.x += 5
    elif keys[pygame.K_UP] and plane1_rect.top > 5:
        plane1_rect.y -= 5
    elif keys[pygame.K_DOWN] and plane1_rect.bottom < screen_height - 5:
        plane1_rect.y += 5

    screen.blit(plane1_image, plane1_rect)
    screen.blit(plane2_image, plane2_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
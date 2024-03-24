import sys, pygame
pygame.init()

fps = pygame.time.Clock()
fps.tick(30)

map = pygame.image.load("images/map.jpg")
map_rect = map.get_rect()
held = False
size = width, height = map.get_width(), map.get_height()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ride the Rails")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        button = pygame.mouse.get_pressed() # Get mouse state
        if button[0]: # Check if left mouse button is pressed
            if held == False: # Check if button is held down
                print(pygame.mouse.get_pos()) # If button is not held down, print true
            held = True # Set held eqaual to true for next iteration
        else: # If left mouse button is not pressed
            held = False # held is set to false, alowing event to happen again

    screen.blit(map, map_rect)
    pygame.display.flip()
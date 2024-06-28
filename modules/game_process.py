import pygame
from .settings import window
from .game_map import *
from .game_objects import *

list_of_fields = render()

is_win = "none"

reset_button = Button(225, 525, 150, 75)

def start():
    global is_win
    global py_map
    global list_of_fields
    turn = "cross"
    game_process = True
    while game_process:
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_process = False
        
        window.blit(background, (0,0))

        mouse_cords = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        for field in list_of_fields:
            if field.is_clicked(mouse_cords[0], mouse_cords[1]) and mouse_buttons[0]:
                if is_win == "none":
                    if field.image == None:
                        
                        field.set_image(turn)
                        if turn == "cross":
                            py_map[field.idy][field.idx] = "X"
                            turn = "zero"
                        else:
                            py_map[field.idy][field.idx] = "O"
                            turn = "cross"
            if field.image != None:
                window.blit(field.image, (field.x+25, field.y+14))
            
        if py_map[0][0] == py_map[0][1] and py_map[0][1] == py_map[0][2] and py_map[0][0] != ".":
            is_win = py_map[0][0]
            list_of_fields[0].image = list_of_fields[0].win_image
            list_of_fields[1].image = list_of_fields[1].win_image
            list_of_fields[2].image = list_of_fields[2].win_image
        elif py_map[1][0] == py_map[1][1] and py_map[1][1] == py_map[1][2] and py_map[1][0] != ".":
            is_win = py_map[1][0]
            list_of_fields[3].image = list_of_fields[3].win_image
            list_of_fields[4].image = list_of_fields[4].win_image
            list_of_fields[5].image = list_of_fields[5].win_image
        elif py_map[2][0] == py_map[2][1] and py_map[2][1] == py_map[2][2] and py_map[2][0] != ".":
            is_win = py_map[1][0]
            list_of_fields[6].image = list_of_fields[6].win_image
            list_of_fields[7].image = list_of_fields[7].win_image
            list_of_fields[8].image = list_of_fields[8].win_image
        elif py_map[0][0] == py_map[1][0] and py_map[1][0] == py_map[2][0] and py_map[0][0] != ".":
            is_win = py_map[0][0]
            list_of_fields[0].image = list_of_fields[0].win_image
            list_of_fields[3].image = list_of_fields[3].win_image
            list_of_fields[6].image = list_of_fields[6].win_image
        elif py_map[0][1] == py_map[1][1] and py_map[1][1] == py_map[2][1] and py_map[0][1] != ".":
            is_win = py_map[0][1]
            list_of_fields[1].image = list_of_fields[1].win_image
            list_of_fields[4].image = list_of_fields[4].win_image
            list_of_fields[7].image = list_of_fields[7].win_image
        elif py_map[0][2] == py_map[1][2] and py_map[1][2] == py_map[2][2] and py_map[0][2] != ".":
            is_win = py_map[0][2]
            list_of_fields[2].image = list_of_fields[2].win_image
            list_of_fields[5].image = list_of_fields[5].win_image
            list_of_fields[8].image = list_of_fields[8].win_image
        elif py_map[0][0] == py_map[1][1] and py_map[1][1] == py_map[2][2] and py_map[0][0] != ".":
            is_win = py_map[0][0]
            list_of_fields[0].image = list_of_fields[0].win_image
            list_of_fields[4].image = list_of_fields[4].win_image
            list_of_fields[8].image = list_of_fields[8].win_image
        elif py_map[0][2] == py_map[1][1] and py_map[1][1] == py_map[2][0] and py_map[0][2] != ".":
            is_win = py_map[0][2]
            list_of_fields[2].image = list_of_fields[2].win_image
            list_of_fields[4].image = list_of_fields[4].win_image
            list_of_fields[6].image = list_of_fields[6].win_image
        window.blit(reset_button.image, (reset_button.x, reset_button.y))
        if reset_button.is_clicked(mouse_cords[0], mouse_cords[1]) and mouse_buttons[0]:
            py_map = [[".",".","."],
                      [".",".","."],
                      [".",".","."]]
            list_of_fields = render()
            is_win = "none"
        pygame.display.flip()
import pygame
from .settings import window
from .game_objects import *

py_map = [[".",".","."],
          [".",".","."],
          [".",".","."]]

def render():
    list_of_fields = []
    for idy, row in enumerate(py_map):
        for idx, column in enumerate(row):
            list_of_fields.append(Field((idx)*145+95, (idy)*145+65, 145, 145, idx, idy))
    return list_of_fields
    
#!/usr/bin/env python

# Example file showing a circle moving on screen
import pygame

from board import Board
from game import Game

pygame.init()


def main():
    # pygame setup
    g = Game(0)
    g.run()



main()

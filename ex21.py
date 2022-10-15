import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex21.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()



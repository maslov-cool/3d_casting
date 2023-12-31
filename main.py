import pygame
'''импортируем PYGAME — это «игровая библиотека», набор инструментов,
 помогающих программистам создавать игры.'''

from settings import *
'''импортируем размеры экрана и доп константы'''

pygame.init()
'''активирует библиотеку pygame'''
screen = pygame.display.set_mode((width, height))
'''активирует экран для отображения'''

clock = pygame.time.Clock()
'''создаём объект, который поможет отслеживать время'''

while True:
    '''цикл для установки желаемых кадров в секунду'''
    '''while True - это когда условие завершения становится известно только в середине итерации.'''
    for event in pygame.event.get():
        '''pygame.event.get() получает события из очереди'''
        if event.type == pygame.QUIT:
            '''pygame.QUIT — событие, которое стартует после нажатия крестика'''
            exit()
        '''exit() вызывает немедленное нормальное завершение программы'''
        screen.fill(black)
        '''fill() для заполнения поверхности'''
        pygame.draw.circle(screen, red, )
        '''рисование игрока'''
        pygame.display.flip()
        '''обновит содержимое всего дисплея'''
        clock.tick()
        '''вычислит, сколько миллисекунд прошло с момента предыдущего вызова'''










import pygame
import numpy as np
import matplotlib.pyplot as plt

#dielectric constant
e_0 = 0.000000000008854187812813

#list of test charges with position and charge Q
objects = [
    {"x_pos": 600, "y_pos": 600, "Q": 1},
    {"x_pos": 400, "y_pos": 500, "Q": 1},
    {"x_pos": 300, "y_pos": 100, "Q": -4},
    {"x_pos": 500, "y_pos": 650, "Q": -1},
    {"x_pos": 780, "y_pos": 700, "Q": 1},
]

#draw field
def draw_field_2d(x_interval, y_interval):
    pygame.init()
    window = pygame.display.set_mode((x_interval, y_interval))
    for y in range(0, y_interval):
        for x in range(0, x_interval):
            E = calc_electric_field_strength(x, y)
            #draw single pixel
            window.set_at((x, y), (max(0, min(255, -round(E) / 5000)), 0, max(0, min(255, round(E) / 5000))))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def print_field(field):
    for i in range(0, len(field)):
        print(i, field[i])

"""
E = (1 / (4 * pi * e_0)) * (Q / r^2)
"""

const_factor = (1 / (4 * np.pi * e_0))

#calculate electric field strength
def calc_electric_field_strength(x, y):
    E = 0
    for object in objects:
        E_single = const_factor * (object["Q"] / (((np.sqrt(((object["x_pos"]-x)**2)+((object["y_pos"]-y)**2))) ** 2)+1))
        E += E_single
    return E

#draw 3d simulation
def draw_field_3d(x_len, y_len):
    fig = plt.figure(figsize=(12, 8))
    ax3d = plt.axes(projection="3d")
    xdata = np.linspace(0, x_len, 100)
    ydata = np.linspace(0, y_len, 100)
    X, Y = np.meshgrid(xdata, ydata)
    Z = calc_electric_field_strength(X, Y)
    ax3d = plt.axes(projection='3d')
    surf = ax3d.plot_surface(X, Y, Z, rstride=7, cstride=7, cmap="viridis")
    fig.colorbar(surf, ax=ax3d)
    ax3d.set_title('electric field')
    ax3d.set_xlabel('X')
    ax3d.set_ylabel('Y')
    ax3d.set_zlabel('Q')
    #plt.savefig('electric_field.png')
    plt.show()

draw_field_2d(1000, 1000)

#draw_field_3d(1000, 1000)

import numpy as np
import matplotlib.pyplot as plt
from functools import reduce


def mid(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return (x1 + x2) / 2, (y1 + y2) / 2


def draw_triangle(t):
    return plt.Polygon(t, color='white')


def dfs(a, b, c, depth):
    if depth == 0:
        return []

    mab = mid(a, b)
    mac = mid(a, c)
    mbc = mid(b, c)

    triangle = [mab, mac, mbc]

    return ([triangle] +
            reduce(lambda x, y: x + y,
                   map(lambda x: dfs(*x, depth - 1),
                       filter(lambda x: x is not None, [(a, mab, mac), (mab, b, mbc), (mac, mbc, c)]))))


def draw(depth):
    l = 50
    a, b, c = (0, 0), (l / 2, (np.sqrt(3) / 2) * l), (l, 0)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(xlim=[0, l], ylim=[0, b[1]])
    ax.set_aspect('equal')
    ax.axis('off')

    triangle = plt.Polygon([a, b, c], color='#343d46')

    ax.add_patch(triangle)

    triangles = dfs(a, b, c, depth)
    for t in triangles:
        patch = draw_triangle(t)
        plt.gca().add_patch(patch)

    plt.show()


draw(6)

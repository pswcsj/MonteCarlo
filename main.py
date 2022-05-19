import random
import matplotlib.pyplot as plt

area_size = 10
num_inner_points = 0
points_x = []
points_y = []
points_z = []
points_color = []
inner_points_x = []
inner_points_y = []
inner_points_z = []
inner_points_color = []

def add_new_point():
    # Create 2D or 3D coordinates
    x = random.uniform(0, area_size)
    y = random.uniform(0, area_size)
    z = random.uniform(0, area_size) # revise this code if necessary
    points_x.append(x), points_y.append(y), points_z.append(z)# revise this code if necessary
    return x, y, z # revise this code if necessary

def is_in(x, y, z): # revise this code if necessary
    global num_inner_points
    if ((x-5)**2 + (y-5)**2 + (z-5)**2) < 5**2:  # check a point is in a circle or sphere here
        num_inner_points += 1 # count the number of points in a circle or sphere here
        return 'blue'
    else:
        return 'red'

def generate_points(n):
    for _ in range(n):
        points_color.append(is_in(*add_new_point()))

def draw_figure_2d(xs = points_x, ys = points_y, color = points_color):
    pi = round(10, 4) # calculate the value of pi here

    fig = plt.figure(figsize=(5, 5))
    plt.scatter(xs, ys,
                c=color, s=1, alpha=0.3,
                label='pi = {}'.format(pi))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show()

def draw_figure_3d(xs = points_x, ys = points_y, zs = points_z, color = points_color):

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs,
                c=color, s=1, alpha=0.3,
                label='pi = {}'.format(pi))
    plt.xlabel('x')
    plt.xlabel('y')
    plt.ylabel('z')
    plt.grid()
    plt.legend()
    plt.show()

def extract_inner_points():
    for x, y, z, c in zip(points_x, points_y, points_z, points_color):
        if c == 'blue':
            # the variables below should contain only the coordinates of inner points
            inner_points_x.append(x)
            inner_points_y.append(y)
            inner_points_z.append(z) # revise this code if necessary
            inner_points_color = [] # revise this code if necessary


if __name__ == '__main__':
    generate_points(50000)
    extract_inner_points()
    draw_figure_3d() # or draw_figure_3d()
    
import pygame as pg

from Objects import Sphere, Plane, Triangle
from Camera import Camera
from Vector import Vector
from Light import Light
from Ray import Ray
from Skybox import Skybox

import random

pg.init()
pg.display.init()

#set screen size
screen_size = Vector(1280, 720)
shadow_bias = 0.0001

#set display
display = pg.display.set_mode((screen_size.x, screen_size.y))
pg.display.set_caption("Python Raytracer")

#set up our camera
camera = Camera(Vector(0, 0, 0), screen_size)
#skybox
skybox = Skybox("skybox.png")


#scene objects
objects = [
    Sphere(Vector(0, 0, -10), 2, Vector(random.random(), random.random(), random.random()), 1),
    Sphere(Vector(5, -1, -5), 3, Vector(random.random(), random.random(), random.random()), 3),
    Sphere(Vector(-3, 1, -10), 1, Vector(random.random(), random.random(), random.random()), 2),
    Sphere(Vector(-7, -2, -20), 4, Vector(random.random(), random.random(), random.random()), 2),
    Plane(Vector(0, 2, 0), Vector(0, -1, 0), Vector(0, 0, 0), 1)
]

#light source
light = Light(Vector(1, 1, 1), 1)

#raytracer function
def raytrace(ray: Ray) -> Vector:
    color = Vector()
    intersect, object = ray.cast(objects)
    normal = False
    reflect = 0
    if intersect:
        normal = object.get_normal(intersect)
        color = object.get_color(intersect)
        reflect = object.get_reflect()
        light_ray = Ray(intersect + normal * shadow_bias, -light.direction.normalize())
        light_intersect, obstacle = light_ray.cast(objects)
        if light_intersect:
            color *= 0.1 / light.intensity
        color *= normal.dot(-light.direction * light.intensity)
    else:
        color = skybox.get_image_coords(ray.direction)
    return color, intersect, normal, reflect

#raytrace
total = pg.display.get_window_size()[1] * pg.display.get_window_size()[0]
for y in range(0, pg.display.get_window_size()[1], 2):
    for x in range(0, pg.display.get_window_size()[0], 2):
        done = y * pg.display.get_window_size()[0] + x
        percent = int(done / total * 100)
        print(f"{percent}%")
        ray = camera.get_direction(Vector(x, y))

        color, intersect, normal, max_reflections = raytrace(ray)
        if intersect:
            reflection_ray = Ray(intersect, ray.direction.reflect(normal))
            reflection_color = Vector(0, 0, 0)
            reflection_counter = 0
            for reflection in range(max_reflections):
                color2, intersect, normal, reflect = raytrace(reflection_ray)
                reflection_color += color2
                reflection_counter += 1
                if intersect:
                    reflection_ray = Ray(intersect, ray.direction.reflect(normal))
                else:
                    break
            color += reflection_color / reflection_counter
        else:
            color = skybox.get_image_coords(ray.direction)

        display.set_at((x, y), color.to_rgb())
        display.set_at((x + 1, y), color.to_rgb())
        display.set_at((x, y + 1), color.to_rgb())
        display.set_at((x + 1, y + 1), color.to_rgb())
    
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

print('done')
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
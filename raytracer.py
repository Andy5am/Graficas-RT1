#Andy Castillo 18040
from mathlib import *
from sphere import *
from math import pi, tan
from materials import *

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
RED = color(255, 0, 0)
BLUE = color(0,0,255)


class Raytracer(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.scene = []
    self.clear()

  def clear(self):
    self.pixels = [
      [BLUE for x in range(self.width)]
      for y in range(self.height)
    ]

  def write(self, filename):
  	writebmp(filename, self.width, self.height, self.pixels)

  def display(self, filename='out.bmp'):
  	self.render()
  	self.write(filename)

  def point(self, x, y, c = None):
    try:
      self.pixels[y][x] = c or self.current_color
    except:
      pass

  def scene_intersect(self, orig, direction):
  	for obj in self.scene:
  		if obj.ray_intersect(orig, direction):
  			return obj.material
  	return None

  def cast_ray(self, orig, direction):
  	impacted_material = self.scene_intersect(orig, direction)
  	if impacted_material:
  		return impacted_material.diffuse
  	else:
  		return BLUE

  def render(self):
    alfa = int(pi/2)
    for y in range(self.height):
      for x in range(self.width):
        i =  (2*(x + 0.5)/self.width - 1)*self.width/self.height*tan(alfa/2)
        j =  (1 - 2*(y + 0.5)/self.height)*tan(alfa/2)
        direction = norm(V3(i, j, -1))
        self.pixels[y][x] = self.cast_ray(V3(0,0,0), direction)


r = Raytracer(900, 900)
r.scene = [
  Sphere(V3(-0.5, -2.1,-9), 0.08, black),
  Sphere(V3(-0.2, -1.9,-9), 0.08, black),
  Sphere(V3(0.2, -1.9,-9), 0.08, black),
  Sphere(V3(0.5, -2.1,-9), 0.08, black),

  Sphere(V3(0, -2.5,-9), 0.2, orange),

  Sphere(V3(0.3, -3.02, -9), 0.05, white),
  Sphere(V3(-0.4, -3.02, -9), 0.05, white),

  Sphere(V3(0.35, -3,-9), 0.1, black),
  Sphere(V3(-0.35, -3,-9), 0.1, black),
  Sphere(V3(0.35, -3,-9), 0.2, eye),
  Sphere(V3(-0.35, -3,-9), 0.2, eye),

  Sphere(V3(0, -0.2,-9), 0.2, black),
  Sphere(V3(0, 0.7,-9), 0.3, black),
  Sphere(V3(0, 1.8,-9), 0.35, black),
  Sphere(V3(0, -2.5,-9), 1.2, white),
	Sphere(V3(0, 0,-9), 1.4, white),
  Sphere(V3(0, 2.7,-11), 2.0, white)
]
r.display()
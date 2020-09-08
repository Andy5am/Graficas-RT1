#Andy Castillo 18040
from mathlib import color

class Material(object):
  def __init__(self, diffuse):
    self.diffuse = diffuse



black = Material(diffuse=color(0, 0, 0))
white = Material(diffuse=color(250, 250, 250))
eye = Material(diffuse=color(220,220,220))
orange = Material(diffuse=color(255, 165, 0))
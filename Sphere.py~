from math import *

class Sphere(object):
	def __init__(self, radius = 1, center_x = 0.0, center_y = 0.0, center_z = 0.0):
		self.radius = radius
		self.center_x = center_x
		self.center_y = center_y
		self.center_z = center_z

	def get_volume(self):
		self.volume = (4 * pi * (self.radius ** 3)) / 3
		return self.volume

	def get_square(self):
		self.square = 4 * pi * (self.radius ** 2)
		return self.square

	def get_radius(self):
		return float(self.radius)

	def get_center(self):
		center = [self.center_x,self.center_y, self.center_z]
		return tuple(center)

	def set_radius(self, r):
		self.radius = r

	def set_center(self, x, y, z):
		self.center_x = x
		self.center_y = y
		self.center_z = z

	def is_point_inside(self, x, y, z):
		if (float(self.center_x) - x) ** 2 + (float(self.center_y) - y) ** 2 + (float(self.center_z) - z) ** 2 < float(self.radius) ** 2:
			return True
		else:
			return False

s2 = Sphere(2)
print s2.get_center()
print s2.get_radius()
print s2.is_point_inside(0, 0.99, 0)
print s2.is_point_inside(1.99, 0, 0)
print s2.is_point_inside(0, 0, 2.99) 
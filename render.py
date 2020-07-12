from data_types_module import dword, 


class Render(object):

	#constructor

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.curr_color = (255, 255, 255)
		self.clear()

	def clear(self):
		self.pixels = [ [BLACK for x in range(self.width)] for y in range(self.height) ]

	def point(self, x, y):
		self.pixels[x][y] = self.curr_color

	def set_color(self, _color):
		self.curr_color = _color

	def write(self, filename):
		archivo = open(filename, 'wb')

		# File header 14 bytes
		archivo.write(char("B"))
		archivo.write(char("M"))
		archivo.write(dword(14+40+self.width*self.height))
		archivo.write(dword(0))
		archivo.write(dword(14+40))

		#Image Header 40 bytes
		archivo.write(dword(40))
		archivo.write(dword(self.width))
		archivo.write(dword(self.height))
		archivo.write(word(1))
		archivo.write(word(24))
		archivo.write(dword(0))
		archivo.write(dword(self.width * self.height * 3))
		archivo.write(dword(0))
		archivo.write(dword(0))
		archivo.write(dword(0))
		archivo.write(dword(0))


		#Pixeles, 3 bytes cada uno

		for x in range(self.height):
			for y in range(self.width):
				archivo.write(self.pixels[x][y])


		#Close file
		archivo.close()




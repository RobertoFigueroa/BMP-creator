from data_types_module import dword, word, char
from utils import color

BLACK = color(0,0,0)
WHITE = color(255,255,255)
RED = color(255,0,0)

class Render(object):

	#constructor
	def __init__(self):
		self.framebuffer = []
		self.curr_color = BLACK

	def glCreateWindow(self, width, height):
		#width and height for the framebuffer
		self.width = width
		self.height = height

	def glInit(self):
		self.curr_color = BLACK

	def glViewport(self, x, y, width, height):
		self.viewportX = x
		self.viewportY = y
		self.viewportWidth = width
		self.viewportHeight = height

	def glClear(self):
		self.framebuffer = [[BLACK for x in range(self.width)] for y in range(self.height)]

	def glClearColor(self, r, g, b):
		clearColor = color( 
				round(r * 255),
				round(g * 255),
				round(b * 255)
			)

		self.framebuffer = [[clearColor for x in range(self.width)] for y in range(self.height)]

	def glVertex(self, x, y):
		#las funciones fueron obtenidas de https://www.khronos.org/registry/OpenGL-Refpages/es2.0/xhtml/glViewport.xml
		X = round((x+1) * (self.viewportWidth/2) + self.viewportX)
		Y = round((y+1) * (self.viewportHeight/2) + self.viewportY)
		self.point(X,Y)

	def glColor(self, r, g, b):
		self.curr_color = color(round(r * 255),round(g * 255),round(b * 255))


	def point(self, x, y):
		self.framebuffer[x][y] = self.curr_color


	def glFinish(self, filename):
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




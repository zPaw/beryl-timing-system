import pygame
from .colors import Color
from .timer import Timer

class CoreDisplay:
	def __init__(self):
		self.running = False

		self.display = None
		self.clock = None
		
		self.width, self.height = (1000, 1000)

		self.timer = None

	def start(self):
		self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()

		self.timer = Timer().load_settings()

		self.running = True
		self.__run__()

	def __run__(self):
		while self.running:
			self.display.fill(Color.white.value)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						if self.timer.timer_running:
							self.timer.stop()
						else:
							self.timer.start()

			if self.timer.timer_running:
				print(self.timer.get_status())

			pygame.display.update()
		pygame.quit()
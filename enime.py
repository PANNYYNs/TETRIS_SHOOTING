class Enime:
	def __init__(self,x,y):
		self.x = x
		self.y = y 
		self.xg = 0
		self.yg = 0
		self.runing_right = False
		self.runing_left = False
		self.runing_gun = False
		self.shot = False

	def set_running(self,mode,value):
		if mode == "Left":
			self.runing_left = value
		elif mode == "Right":
			self.runing_right = value
		elif mode == "Gun":
			self.runing_gun = value

	def get_running(self,mode):
		if mode == "Left":
			return self.runing_left
		elif mode == "Right":
			return self.runing_right
		elif mode == "Gun":
			return self.runing_gun


	def get_x(self):
		return self.x

	def set_x(self,value):
		self.x = value

	def get_y(self):
		return self.y

	def set_y(self,value):
		self.y = value

	def get_shot(self):
		return self.shot

	def set_shot(self,value):
		self.shot = value

	def get_xg(self):
		return self.xg

	def set_xg(self,value):
		self.xg = value

	def get_yg(self):
		return self.yg

	def set_yg(self,value):
		self.yg = value
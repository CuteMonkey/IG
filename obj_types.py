#This code contains all (build-in) types of variables.
import string
from random import *

################################################3

def randomstring(string_len):
	characters = string.ascii_letters + string.punctuation + string.digits
	password=""
	for x in range(randint(1,string_len)):
    		password =password+"".join(choice(characters))
	return password

class VarString:
	def __init__(self):
		self._len = 10
		self._string = ''
	def	gen_val(self):
		self._string = randomstring(self._len) 
	def set_len(self,_len):
		self._len=_len
	def get_val(self):
		return self._string








###########################################

class VarInt:
	def __init__(self):
		self.__val = 0        #defult value
		self.__max = 2**64    #default max
		self.__limit_max = None  #the limited max from the original max
		self.__max_flag = False
		self.__min = -(2**64) #default min
		self.__limit_min = None  #the limited min from the original min
		self.__min_flag = False
		self.__width = 0      #the width of range
		self.__base = 10      #base options: 2, 8, 10, 16
		self._type = 'int'    #read-only
		self._limit_pows = (1/5, 1/5, 2/5, 2/5, 3/5, 3/5, 4/5, 4/5, 1, 1)  #read-only
		self._gen_count = 0   #read-only
	def set_max(self, _max):
		if self.__max_flag:
			if _max < self.__max:
				self.__max = _max
		else:
			self.__max = _max
			self.__max_flag = True
	def set_min(self, _min):
		if self.__min_flag:
			if self.__min < _min:
				self.__min = _min
		else:
			self.__min = _min
			self.__min_flag = True
	def set_base(self, base):
		pass
	def get_val(self):
		if self.__base == 2:
			pass
		elif self.__base == 8:
			pass
		elif self.__base == 10:
			return self.__val
		elif self.__base == 16:
			pass
	def gen_val(self):
		if self.__min < self.__max:
			if self._gen_count < 10:
				self.__width = self.__max - self.__min
				self.__limit_max = int(0 + self.__width ** self._limit_pows[self._gen_count])
				if self.__limit_max > self.__max:
					self.__limit_max = self.__max
				self.__limit_min = int(0 - self.__width ** self._limit_pows[self._gen_count])
				if self.__limit_min < self.__min:
					self.__limit_min = self.__min
				self.__val = random.randint(self.__limit_min, self.__limit_max)
				self._gen_count = self._gen_count + 1
				return True
			else:
				self.reset()
		else:
			return False
	def reset(self):
		self._gen_count = 0
	def prime(self):  #generate a prime number value
		pass

class RelStmt:  #this class handles relation statements
	def _init_(self):
		self.l_operand = None #left object number
		self.r_operand = None #right object number
		self.operator = None  #operator type
		

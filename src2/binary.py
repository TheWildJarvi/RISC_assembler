class binary_value():

	def int_to_array(self, value, length):
		if value < 0:
			self.sign = -1
			value = value * -1
		array = []
		while value > 0:
			if value % 2 == 0:
				array = [False] + array
			else:
				array = [True] + array
			value = int(value / 2)
			if length > 0 and len(array) > (length - 1)  :
				return array
		return [True for i in range(length-len(array))]+array

	def __init__(self, value, length= -1 ):
		self.value = []
		self.length = 0
		self.sign = 1
		if isinstance(value, int):
			self.value = self.int_to_array(value, length)
		elif isinstance(value, str):
			print('string')
		self.length = len(self.value)

	def __repr__(self):
		representation = 'Positive \n' if (self.sign == 1) else 'Negative \n'
		representation = representation + 'Absolute representation: ' + repr(self.value) +'\n'
		representation = representation + repr(self.length)
		return representation

	def set_mag(self, number):
		if self.length <= number:
			self.value = [False for i in range(number-self.length)]+self.value
		else:
			self.value = self[:number]
		self.length = number

#def and_op(a: binary_value, b: binary_value):
#	b.set_mag(a.length) if a.length > b.length else a.set_mag(b.length)
#	return [a.value[i] and b.value[i] for i in range(a.length)]

#def or_op(a: binary_value, b: binary_value):
#	b.set_mag(a.length) if a.length > b.length else a.set_mag(b.length)
#	return [a.value[i] or b.value[i] for i in range(a.length)]

		
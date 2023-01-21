# Practical lesson No. 5, task No. 1.
# This program defines the variable x at the global, enclosing, local level.

x = 12

print(f'GLOBAL x = {x}')

def enclosing_level():

	x = 13

	print(f'ENCLOSING x = {x}')

	def local_level():

		x = 14

		print(f'LOCAL x = {x}')

	local_level()

	print(f'ENCLOSING x = {x}')

enclosing_level()
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from numbers import Number
from decimal import Decimal
'''
http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-1.html

1- Definir una función max() que tome como argumento dos números y devuelva el
mayor de ellos. (Es cierto que python tiene una función max() incorporada,
pero hacerla nosotros mismos es un muy buen ejercicio.
'''

class EjerciciosPythonDiario:
	'''
	Diez ejercicios prácticos de Python

	'''

	def __init__(self):
		True


	# Function max_function
	def max_function(first_value, second_value):
		'''
		Compare two numbers (integer or decimal) and return the bigger one
		'''
		try:
			# Validate if both inputs are numbers (int or decimal)
			if type(first_value) == int or type(first_value) == float and \
			type(second_value) == int or type(second_value) == float:
				# Compare the two numbers
				if first_value > second_value:
					# If the first value is bigger than the second, then stop
					answer = first_value
				else:
					# Otherwise, the second value is bigger
					answer = second_value
			else:
				# Input is far beyond a number
				answer = 'Function values are not numbers. x('
		except Exception as e:
			raise

		return answer

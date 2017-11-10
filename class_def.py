class Converter:

	def __init__(self, n1, n2):											# Constructor intialises both the number systems
		self.N1 = n1 													# N1 - Base characters of number system 1
		self.N2 = n2 													# N2 - Base characters of number system 2

	def convert_to_decimal(self, n):									# Converts from number system 1 to decimal number system 
		d = {}
		for i in range(len(self.N1)):									
			d[self.N1[i]]=i
		sum_decimal=0
		length=len(self.N1)												# Base = value of vaiable length
		for i in range(len(n)):
			sum_decimal = sum_decimal + (d[n[i]]*((length)**(len(n)-i-1)))
		return sum_decimal

	def convert_to_base(self, decimal_num):								# Converts from decimal number system to number system 2
		if(decimal_num == 0):
			return [self.N2[0]]	
		l = []															# List that keeps remainder when divided by base
		base = len(self.N2)
		tmp_num = decimal_num
		while(tmp_num!=0):
			remainder = (tmp_num%base)
			tmp_num/=base
			l.append(remainder)
		l.reverse()

		d = {}															# Maps base characters to numbers
		for i in range(len(self.N2)):
			d[self.N2[i]] = i
		rev_d = {}														# Reverse the above mapping
		for i in d:
			rev_d[d[i]] = i
		l_characters = []

		for i in l:
			for k in rev_d:
				if(i==k):
					l_characters.append(rev_d[k])
		return l_characters				

	def __convert__(self, n):											# Private function that calls the above two functions
		return self.convert_to_base(self.convert_to_decimal(n))

	def call_convert(self, n):											# Function to call private function __convert__()
		return self.__convert__(n)

class Calculater(Converter):											# Calculator class inherits properties of Convert class
	
	def __init__(self, n):												# Constructor intialises both the number system to the same number system
		self.N1 = n
		self.N2 = n			
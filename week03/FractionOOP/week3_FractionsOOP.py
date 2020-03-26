from math import gcd

class Fraction:
	def __init__(self,num,denom):
		assert denom>=1,'Zero or negative denominator'

		#if denom<1:
			#raise AssertionError('Zero or negative denominator')

		self.num=num
		self.denom=denom

	def __str__(self):
		return f'{self.num}/{self.denom}'

	def __repr__(self):
		return f'Fraction {self}'

	def __eq__(self,other):

		simplified_self=self.simplify()
		simplified_other=other.simplify()

		return simplified_self.num==simplified_other.num and\
		 simplified_self.denom==simplified_other.denom

	def simplify(self):
		divider=gcd(self.num,self.denom)

		return Fraction(self.num//divider, self.denom//divider)

	def __add__(self,other):
		
		if self.denom==other.denom:
			num=self.num+other.num
			denom=other.denom
		else:
			num=self.num*other.denom+self.denom*other.num
			denom=self.denom*other.denom


		return Fraction(num,denom).simplify()

	def __gt__(self,other):
		simplified_self=self.simplify()
		simplified_other=other.simplify()

		dive1=simplified_self.num/simplified_self.denom
		dive2=simplified_other.num/simplified_other.denom

		if dive1>dive2:
			return True
		else:
			return False

	def sort_function(fractions):

		list_of=sorted(fractions)
		return list_of
		


def main():
	pass
if __name__ == '__main__':
    main()
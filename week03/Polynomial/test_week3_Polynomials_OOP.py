import unittest
from week3_Polynomials_OOP import Polynomial
from week3_Polynomials_OOP import Term

class TestTerm(unittest.TestCase):
	def test_len_of_term(self):
		term1=Term('2x+2')

		self.assertEqual(len(term1),4)

	def test_Term_create_if_it_is_zero(self):
		term1=Term('2')

		result=Term.create_Terms_of_derives(term1)

		self.assertEqual(result,[])

	def test_Term_create_if_it_is_with_coefficitent_and_x(self):
		term1=Term('2x')

		result=Term.create_Terms_of_derives(term1)

		self.assertEqual(result,['2'])

	def test_Term_create_if_it_is_with_x(self):
		term1=Term('x')

		result=Term.create_Terms_of_derives(term1)

		self.assertEqual(result,['1'])

class TestPolynomial(unittest.TestCase):
	def test_len_of_Polynomial(self):
		term1=Polynomial('2x+2')

		self.assertEqual(len(term1),4)

	def test_if_it_returns_derivetive_of_coefficient(self):
		term1=Polynomial('2')
		result=Polynomial.create_list_of_terms(term1)
		self.assertEqual(result,"f'(x)=0")

	def test_if_it_returns_derivetive_of_coefficient_only_x(self):
		term1=Polynomial('x')
		result=Polynomial.create_list_of_terms(term1)
		self.assertEqual(result,"f'(x)=1")


	def test_if_it_returns_derivetive_of_coefficient_one(self):
		term1=Polynomial('2x^3')
		result=Polynomial.create_list_of_terms(term1)
		self.assertEqual(result,"f'(x)=6x^2")

	def test_if_it_returns_derivetive_of_coefficient_two_coef(self):
		term1=Polynomial('2x^3+2')
		result=Polynomial.create_list_of_terms(term1)
		self.assertEqual(result,"f'(x)=6x^2")

	def test_if_it_returns_derivetive_of_coefficient_two_coef_sum(self):
		term1=Polynomial('2+2')
		result=Polynomial.create_list_of_terms(term1)
		self.assertEqual(result,"f'(x)=0")



if __name__=='__main__':
	unittest.main()


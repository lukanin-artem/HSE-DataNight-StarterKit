import unittest
import test

class TestMyTest(unittest.TestCase):
	def test_test(self):
		self.assertTrue(test.test())

if __name__ == '__main__':
	unittest.main()

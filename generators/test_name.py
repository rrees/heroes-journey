import unittest

from . import name

class TestNames(unittest.TestCase):
	def test_name_is_created(self):
		generated_name = name.create_name()

		self.assertTrue(len(generated_name) > 0)
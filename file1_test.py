import unittest
from file1 import Fiber

class TestFiber(unittest.TestCase):
    """Test for Fiber class"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print('setUp')
        self.flax = Fiber('Flax', '20', 'Coarse')
        self.corn = Fiber('Corn', '80', 'Silken')

    def tearDown(self):
        print('tearDown\n')

    def test_micron(self):
        self.assertEqual(self.flax.micron, '20')
        self.assertEqual(self.corn.micron, '80')

    def test_texture(self):

        self.assertEqual(self.flax.texture, 'Coarse')
        self.assertEqual(self.corn.texture, 'Silken')

if __name__ == '__main__':
    unittest.main()
import os
import sys
import pytest
import unittest

sys.path.append('../ConsoleApp')
import Product as product



class Testing(unittest.TestCase):
    
    def test_addProduct(self):
        self.assertEqual(product.Product.addProduct(5), 6)

    def test_removeProduct(self):
        self.assertEqual(product.Product.removeProduct(5), 4)


if __name__ == '__main__':
    unittest.main()

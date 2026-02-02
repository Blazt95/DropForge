# test_dropforge.py
"""
Tests for DropForge module.
"""

import unittest
from dropforge import DropForge

class TestDropForge(unittest.TestCase):
    """Test cases for DropForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DropForge()
        self.assertIsInstance(instance, DropForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DropForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

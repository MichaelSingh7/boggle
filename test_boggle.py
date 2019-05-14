import unittest
import boggle


class TestBoggle(unittest.TestCase):
    """
    Our Test Suite For Boggle Solver
    """
    
    def test_can_create_an_empty_grid(self):
        """
        Test To See If We Can Create An Empty Grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
    
    
    def test_grid_size_is_width_times_height(self):
        """
        Test Is To Ensure That The Total Size Of The Grid 
        Is Equal To Width * Height
        """
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)
        
        
    def test_grid_coorindates(self):
        """
        Test To Ensure That All Of The Coordinates
        Inside Of The Grid Can Be Accessed
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        
        
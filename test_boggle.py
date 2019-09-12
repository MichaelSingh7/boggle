import unittest
import boggle
from string import ascii_uppercase

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
        
    
    def test_grid_is_filled_with_letters(self):
        """
        Ensure That Each Of The Coordinates In The Grid
        Contains Letters
        """
        
        grid = boggle.make_grid(2,3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
    def test_neighbours_of_a_position(self):
        """
        Ensure That A Position Has 8 Neighbours
        """
        coords = (1,2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
    
    
    def test_all_grid_neighbours(self):
        """
        Ensure That All Of The Grid Positions Have Neighbours
        """
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        for pos in grid:
            others = list(grid) # Creates A New List From The Dictionary's Keys
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
            
            
    def test_converting_a_path_to_a_word(self):
        """
        Ensure That Paths Can Be Converted To Words
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        
    def test_search_grid_for_words(self):
        """
        Ensure That Certain Patterns Can Be Found In A Path_To_Word
        """
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        
        fullwords = [twoLetterWord, threeLetterWord, notThereWord]
        stems = ['A', 'AB', 'E', 'EE']
        dictionary = fullwords, stems
        
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
        
        
    def test_load_dictionary(self):
        """
        Test That The 'Get_Dictionary' Function Returns A Dictionary
        That Has A Length Greater Than 0
        """
        dictionary = boggle.get_dictionary('words.txt')
        self.assertGreater(len(dictionary), 0)
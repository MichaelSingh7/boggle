from string import ascii_uppercase
from random import choice 


def make_grid(width, height):
    """
    Creates A Grid That Will Hold All Of The Tiles
    For A Boggle Game
    """
    return {(row, col): choice(ascii_uppercase)
        for row in range(height)
        for col in range(width)}
    
    
def neighbours_of_position(coords):
    """
    Get Neighbours Of A Give Position
    """
    row = coords[0]
    col = coords[1]
    
    # Assign Each Of The Neighbours
    # Top-Left To Top-Right.
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row -1, col + 1)
    
    # Left To Right
    left = (row, col - 1)
    # The `(row, col)` Coordinates Passed To This
    # Function Are Situated Here
    right = (row, col + 1)
    
    # Bottom-Left To Bottom-Right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_left, top_center, top_right,
             left, right,
             bottom_left, bottom_center, bottom_right]
             
             
def all_grid_neighbours(grid):
    """
    Get All Of The Possible Neighbours For Each Position In
    The Grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours    
    
    
def path_to_word(grid, path):
    """
    Add All Of The Letters On The Path To A String
    """
    return ''.join([grid[p]  for p in path])
    
    
def search(grid, dictionary):
    """ m
    Search Through The Paths To Locate Words By Matching
    Strings To Words In A Dictionary
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary
    
    def do_search(path):
        word = path_to_word(grid, path)
        if word in full_words:
            paths.append(path)
        if word not in stems:
            return 
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path: 
             do_search(path + [next_pos])
             
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    
    
def get_dictionary(dictionary_file):
    """
    Load Dictionary File
    """
    full_words, stems = set(), set()
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
                
    return full_words, stems            
        
def main():
    """
    This Is The Function That Will Run The Whole Project
    """
    grid = make_grid(4, 4)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    for word in words:
        print(word)
    print("Found %s words" % len(words)) 
    

if __name__ == "__main__":
    main()
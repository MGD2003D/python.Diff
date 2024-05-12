import unittest
from src.lab3.sudoku import read_sudoku, solve, check_solution, generate_sudoku, get_row, get_col, get_block, find_empty_positions, find_possible_values

class TestSudoku(unittest.TestCase):
    def test_read_sudoku(self):
        grid = read_sudoku("puzzle1.txt")
        self.assertEqual(len(grid), 9)
        self.assertEqual(len(grid[0]), 9)

    def test_solve(self):
        grid = read_sudoku("puzzle1.txt")
        solution = solve(grid)
        self.assertTrue(check_solution(solution))

    def test_check_solution(self):
        grid = read_sudoku("puzzle1.txt")
        solution = solve(grid)
        self.assertTrue(check_solution(solution))

    def test_get_row(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(get_row(grid, (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row(grid, (1, 0)), ['4', '5', '6'])

    def test_get_col(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(get_col(grid, (0, 2)), ['.', '6', '9'])

    def test_get_block(self):
        grid = [['5', '3', '.', '6', '.', '.', '.', '9', '8'],
                ['.', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '.', '8', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '4', '.', '.', '7', '.', '.'],
                ['.', '6', '.', '8', '.', '3', '.', '2', '.'],
                ['.', '.', '3', '.', '.', '1', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['3', '.', '.', '.', '8', '.', '.', '7', '9']]
        self.assertEqual(get_block(grid, (1, 2)), ['5', '3', '.', '.', '.', '.', '.', '.', '8'])

    def test_find_empty_positions(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(find_empty_positions(grid), (0, 2))

    def test_find_possible_values(self):
        grid = read_sudoku("puzzle1.txt")
        empty_pos = find_empty_positions(grid)
        possible_values = find_possible_values(grid, empty_pos)
        self.assertIsInstance(possible_values, set)

    def test_generate_sudoku(self):
        grid = generate_sudoku(40)
        empty_cells = sum(1 for row in grid for e in row if e == '.')
        self.assertEqual(empty_cells, 41)
        solution = solve(grid)
        self.assertTrue(check_solution(solution))

if __name__ == "__main__":
    unittest.main()
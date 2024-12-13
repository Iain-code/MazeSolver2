from graphics import Cell, Window, Point, Line
import time
import random


class Maze:
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):

        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

            
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
        
    def _draw_cell(self, i , j):
        if self._win is None:
            return
        x_position = self.x1 + (i * self.cell_size_x)
        y_position = self.y1 + (j * self.cell_size_y)

        x_position_end = x_position + self.cell_size_x
        y_position_end = y_position + self.cell_size_y
  
        self._cells[i][j].draw(x_position, y_position, x_position_end, y_position_end)
        self._animate()

    def _animate(self):

        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False

        x = self.num_cols - 1
        y = self.num_rows - 1
        self._draw_cell(x, y)

        
    def _break_walls_r(self, i, j): # i and j are Cell objects 
        
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            if i + 1 < self.num_cols and self._cells[i + 1][j].visited == False:
                to_visit.append((i + 1, j))
            if i - 1 >= 0 and self._cells[i - 1][j].visited == False:
                to_visit.append((i - 1, j))
            if j + 1 < self.num_rows and self._cells[i][j + 1].visited == False:
                to_visit.append((i, j + 1))
            if j - 1 >= 0 and self._cells[i][j - 1].visited == False:
                to_visit.append((i, j - 1))
            
            if not to_visit:
                self._draw_cell(i, j)
                return
            
            random_cell = random.randrange(len(to_visit))
            next_index = to_visit[random_cell]
            
            if next_index == (i + 1, j):
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index == (i - 1, j):
               self._cells[i][j].has_left_wall = False
               self._cells[i - 1][j].has_right_wall = False
            if next_index == (i, j + 1):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index == (i, j - 1):
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                
            self._break_walls_r(next_index[0], next_index[1])


    def _reset_cells_visited(self):

        for rows in self._cells:
            for cell in rows:
                cell.visited = False
    
    def solve(self):

        i = 0
        j = 0

        self._solve_r()
    
        if self._solve_r(i, j):
            return True
        else:
            return False    

    def _solve_r(self, i, j):
        
        self._animate()
        self._cells[i][j].visited = True

        if self._cells[i][j] == self._cells[-1][-1]:
            return True

        



            
    

              
        

         
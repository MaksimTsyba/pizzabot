import re
import sys


class Pizzabot:
    """ Generate instruction for Pizzabot """

    def __init__(self, input_data):
        self.input_data = input_data
        self.grid_size_x, self.grid_size_y = self.prepare_grid_size()
        self.grid_points = self.prepare_grid_points()

    def prepare_grid_size(self) -> tuple:
        """ Get grid size"""

        grid_size = re.findall('(\d+x\d+)', self.input_data)[0].split('x')
        return tuple([int(grid_size_item) for grid_size_item in grid_size])

    def prepare_grid_points(self) -> tuple:
        """ Get grid points """

        grid_points = re.findall('(\d*,\d*)', self.input_data)
        prepared_grid_points = list()
        for roughly_grid_point_item in grid_points:
            prepared_grid_points.append(tuple([int(value_item) for value_item in roughly_grid_point_item.split(',')]))
        return tuple(prepared_grid_points)

    def validate_grid_points(self) -> bool:
        """ Validate values for fit in grid size """
        for grid_points_item in self.grid_points:
            grid_point_x, grid_point_y = grid_points_item
            if self.grid_size_x < grid_point_x or self.grid_size_y < grid_point_y:
                raise Exception(f"Value ({grid_point_x}, {grid_point_y}) "
                                f"don't fit to grid size {self.grid_size_x}x{self.grid_size_y}")
        return True

    def generate_instruction(self) -> str:
        """ Generate instruction for Pizzabot  """

        if self.validate_grid_points():
            start = (0, 0)
            result = ''
            for grid_points_item in self.grid_points:
                grid_point_x, grid_point_y = grid_points_item
                start_x, start_y = start
                move_x = grid_point_x - start_x
                move_y = grid_point_y - start_y
                result += 'E' * move_x if move_x > 0 else 'W' * (move_x * -1)
                result += 'N' * move_y if move_y > 0 else 'S' * (move_y * -1)
                result += 'D'
                start = grid_points_item

            return result

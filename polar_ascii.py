import importlib.util
import math
import os
import sys

# number of points per degree in the domain
ITERATION_MULTIPLE = 10

# Ensure script is called with path to equation file
if len(sys.argv) != 2:
    raise ValueError("Script must be called with one and only one argument")

# Load equation file
spec = importlib.util.spec_from_file_location("equation", sys.argv[1])
if spec is None:
    raise ValueError("Invalid file provided")

equation = importlib.util.module_from_spec(spec)
sys.modules["equation"] = equation

loader = spec.loader
if loader is None:
    raise ValueError("Invalid file provided")

loader.exec_module(equation)

# Generate raw cartesian points from equation file
raw_points: list[tuple[float, float]] = []
inc_count = (
    ITERATION_MULTIPLE
    * int((equation.domain[1] - equation.domain[0]) * (180.0 / math.pi))
    + 1
)
for inc in range(inc_count):
    theta = (
        (inc / inc_count) * (equation.domain[1] - equation.domain[0])
    ) + equation.domain[0]

    r = equation.r(theta)
    cart_point = (r * math.cos(theta), r * math.sin(theta))
    raw_points.append(cart_point)


x_min = float(min(raw_points, key=lambda point: point[0])[0])
x_min_max_diff = float(max(raw_points, key=lambda point: point[0])[0]) - x_min
y_max = float(max(raw_points, key=lambda point: point[1])[1])
y_min_max_diff = y_max - float(min(raw_points, key=lambda point: point[1])[1])

terminal_size = os.get_terminal_size()

# Cells have a width of two characers
# Remove one line to make room for new terminal prompt
grid_size = (terminal_size.columns // 2, terminal_size.lines - 1)


scale = min(grid_size[0] / x_min_max_diff, grid_size[1] / y_min_max_diff)


final_points: list[tuple[float, float]] = []
for point in raw_points:
    new_x = (point[0] - x_min) * scale
    new_y = (point[1] - y_max) * -scale
    final_points.append((new_x, new_y))

grid = [[False] * grid_size[0] for _ in range(grid_size[1])]

for point in final_points:
    try:
        grid[int(point[1])][int(point[0])] = True
    except IndexError:
        print("Hit bound, cont.")

for row in grid:
    for cell in row:
        if cell:
            print("XX", end="")
        else:
            print("  ", end="")
    print("")

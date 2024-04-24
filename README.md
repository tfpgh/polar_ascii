# polar_ascii

`polar_ascii` graphs arbitrary polar functions in ASCII. It automatically scales the function over the given domain to fit within the terminal window.

I made this project over the course of about an hour to learn more about polar functions.


## Examples
`heart.py`
![Heart Example](demos/heart.gif)
`spiral_medium.py`
![Spiral Medium Example](demos/spiral_medium.gif)
`flower.py`
![Flower Example](demos/flower.gif)

## Usage

To graph a polar function, pass a python file defining the variable `domain` and function `r` into `polar_ascii.py`

Example function file (`examples/spiral_medium.py`):
```python
import math

domain: tuple[float, float] = (0.0, 5 * math.pi)


def r(theta: float) -> float:
    return theta
```

Call it with:
```zsh
python3 polar_ascii.py examples/spiral_medium.py
```
(or the path to your function file)

# polar_ascii

`polar_ascii` graphs arbitrary polar functions in ASCII. It automatically scales the function over the given domain to fit within the terminal window.

## Examples
`heart.py`
<br>
<img alt="Heart Example" src="demos/heart.gif" width="500px">
<br>
`spiral_medium.py`
<br>
<img alt="Spiral Medium Example" src="demos/spiral_medium.gif" width="500px">
<br>
`flower.py`
<br>
<img alt="Flower Example" src="demos/flower.gif" width="500px">
<br>

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

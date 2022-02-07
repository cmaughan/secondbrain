from typing import Tuple
import math
import numpy as np

def clamp(value, min_val = 0.0, max_val = 255.0) -> float:
    if np.isnan(value):
        return 0.0
    # use rounding to better represent values between max and min
    return float(round(max(min(value, max_val), min_val)))

#https://github.com/esemeniuc/kelvin_rgb/blob/master/kelvin_rgb/__init__.py
# see http://www.zombieprototypes.com/?p=210 for plot and calculation of coefficients
def k_to_rgb(kelvin: int) -> Tuple[float, float, float]:
    temperature = kelvin / 100.0

    if temperature < 66.0:
        red = 255
    else:
        red = temperature - 55.0
        red = 351.97690566805693 + 0.114206453784165 * red - 40.25366309332127 * math.log(red)

    # Calculate green
    if temperature < 66.0:
        green = temperature - 2
        green = -155.25485562709179 - 0.44596950469579133 * green + 104.49216199393888 * math.log(green)
    else:
        green = temperature - 50.0
        green = 325.4494125711974 + 0.07943456536662342 * green - 28.0852963507957 * math.log(green)

    # Calculate blue
    if temperature >= 66.0:
        blue = 255
    elif temperature <= 20.0:
        blue = 0
    else:
        blue = temperature - 10
        blue = -254.76935184120902 + 0.8274096064007395 * blue + 115.67994401066147 * math.log(blue)

    return [clamp(red, 0, 255) / 255.0, clamp(green, 0, 255) / 255.0, clamp(blue, 0, 255) / 255.0]
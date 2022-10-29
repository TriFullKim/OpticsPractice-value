import numpy as np
import pandas as pd

ORIGIN_VALUE = -0.7
ATTEMPT = [i+1 for i in range(3)]
lens_1p52 = {
    'd[mm]': [1.305, 1.280, 1.295],
    'K_1': [-4.89, -4.8, -4.87],
    'K_2': [-4.87, -4.75, -4.75],
    'h[mm]': [-5.5-ORIGIN_VALUE, -5.75-ORIGIN_VALUE, -5.63-ORIGIN_VALUE]
}
lens_1p56 = {
    'd[mm]': [1.155, 1.154, 1.154],
    'K_1': [-6.8, -7.3, -6.5],
    'K_2': [-7.2, -6.9, -5.75],
    'h[mm]': [-6.7-ORIGIN_VALUE, -6.62-ORIGIN_VALUE, -6.62-ORIGIN_VALUE]
}
prism_1p5 = {'size': [4, 4, 4]}
focusDistance = {'a[mm]': [150.34, 144.58, 149.56]}

LENS_1p52_DATA = pd.DataFrame(lens_1p52,index=ATTEMPT)
LENS_1p56_DATA = pd.DataFrame(lens_1p56,index=ATTEMPT)
PRISM_1p5 = pd.DataFrame(prism_1p5,index=ATTEMPT)
FOCUS_DISTANCE = pd.DataFrame(focusDistance,index=ATTEMPT)

LENS_1p52_DATA['n'] = 1.52
LENS_1p56_DATA['n'] = 1.56
PRISM_1p5['n'] = 1.50

print(
    LENS_1p52_DATA, LENS_1p56_DATA, PRISM_1p5, FOCUS_DISTANCE,
    '=====DATA=====',
    LENS_1p52_DATA.mean(),
    LENS_1p56_DATA.mean(),
    PRISM_1p5.mean(),
    FOCUS_DISTANCE.mean(),
    sep='\n\n\n'
)
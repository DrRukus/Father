#!/usr/bin/env python

import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file
from bokeh.palettes import brewer, all_palettes

N = 20
categories = ['y' + str(x) for x in range(10)]

data = {}
data['x'] = np.arange(N)
for cat in categories:
    data[cat] = np.random.randint(10, 100, size=N)

df = pd.DataFrame(data)
df = df.set_index(['x'])

def stacked(df, categories):
    areas = dict()
    last = np.zeros(len(df))
    for cat in categories:
        next = last + df[cat]
        areas[cat] = np.hstack((last[::-1], next))
        last = next
    return areas

areas = stacked(df, categories)

#for palette, _ in all_palettes['Inferno'].items():
#    print(palette)
#colors = brewer['PuBuGn'][len(areas) - 1]
colors = all_palettes['Inferno'][len(areas)]
#colors = brewer['Spectral'][3]
print(colors)

x2 = np.hstack((data['x'][::-1], data['x']))

p = figure(x_range=(0, 19), y_range=(0, 800))
p.grid.minor_grid_line_color = '#eeeeee'

p.patches([x2] * len(areas), [areas[cat] for cat in categories],
          color=colors, alpha=0.8, line_color=None)

output_file("brewer.html", title="brewer.py example")

show(p)
#!/usr/bin/env python

import sys
print(sys.path)
sys.path.append('/usr/local/bin')
import pandas as pd
import numpy as np
import holoviews as hv
hv.extension('bokeh')

stationInfo = pd.read_csv('station_info.csv')
print(stationInfo.head())

scatter = hv.Scatter(stationInfo, kdims=['services'], vdims=['ridership'])
print(scatter)
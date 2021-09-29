# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:07:49 2021

@author: s2916320
"""

import pandas as pd
dfSDG = pd.read_excel('C:/Users/s2916320/Downloads/Goal8.xlsx', usecols=['GeoAreaName', 'TimePeriod', 'Value','Type of product'])
# dfSDG.set_index('Type of product', inplace= True, drop= True)
dfSDGsubset = dfSDG.loc[dfSDG['Type of product'] == 'FOF']
dfSDGsubset = dfSDGsubset.pivot(index='TimePeriod', columns=['GeoAreaName','Type of product'], values= ['Value'])
pd.isna(dfSDGsubset).sum()
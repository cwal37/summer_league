# -*- coding: utf-8 -*-
"""
Created on Thu May 26 09:51:41 2016

@author: wal
"""
import pdb
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects

plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 16
plt.style.use('ggplot')
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 14}

matplotlib.rc('font', **font)


tc_dict = {'Avril LaGreen':['#12D300', '#FF0000'],
           'SWAg':['#EFEFEF','#FF0000'],
           'Mediokra':['#38761D', '#FFFF00'],
           'MAGA':['#999999','#FF9900'],
           'Cheerwine?':['#CC0000','#FF9900'],
           'Blue Ridge':['#0000FF','#FF9900'],
           'ThunderPants':['#000000','#FF0000'],
           'Victorious Secret':['#FF00FF','#000000'],
           'US!':['#01D7FF','#FFFF00'],
           'Vanilla Whoopass':['#FFFFFF','#FF9900'],
           'deR':['#FF0000','#FFFF00'],
           'Purple Reign':['#9900FF','#FFFF00'],
           'Rubber Huckies':['#FFFF00','#38761D'],
           'Call Me Navy':['#1C4587','#FF9900']}


df = pd.read_csv('cumulative_records.csv')
df = df.ix[1:4,:]

games = [0,1,2,3]

for x in tc_dict:
    
    print x
    team_df =  df[x]
    #pdb.set_trace()
    plt.plot(games, team_df, label = x, color = tc_dict[x][0], linewidth=5,
             path_effects=[path_effects.SimpleLineShadow(shadow_color = tc_dict[x][1], alpha = 0.5), path_effects.Normal()])

    
    
    #print tc_dict[x][0]
plt.xticks(games, ['Pre-Season', 'Game 1', 'Game 2', 'Game 3'])
plt.title('2016 Summer League Cumulative Point Differential Through Week 3')
plt.ylabel('Points')
#plt.xlabel('Games')
plt.gcf().subplots_adjust(bottom=0.16)

legend = plt.legend( loc='upper center', bbox_to_anchor=(0.5, -0.04),fancybox=True, shadow=True, ncol=3)
plt.savefig('cumulative_point_diff.png', dpi = 400)
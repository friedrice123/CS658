import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

var = 'WEVTS_RCSOFF_GOFF'

df_stat = pd.read_csv('CSV_Dataset\Stat\S_'+var+'_CS.csv')
df_top_cs = pd.read_csv('CSV_Dataset\Top\T_'+var+'_CS.csv')
df_td = pd.read_csv('CSV_Dataset\Time Delta\TD_'+var+'.csv')
df_stat_cs = df_stat[df_stat['id'] != 'GS_1']
df_stat_cs = df_stat_cs.reset_index(drop=True)
df_stat_cs.drop(['sampling_count','simulation_time','sampling_resolution'], axis=1, inplace=True)
df_top_cs.drop(['sampling_count','simulation_time','sampling_resolution'], axis=1, inplace=True)
df_td.drop(['sampling_count','simulation_time','sampling_resolution'], axis=1, inplace=True)
df_combined = df_top_cs.merge(df_stat_cs, on=['id','condition'], how='left')
df_combined.to_csv('CSV_Dataset\Combined_wo_TD\Combined_'+var+'_CS.csv', index=False)

df_combined2 = df_stat.merge(df_td, on=['id','condition'], how='left')
df_combined3 = df_top_cs.merge(df_combined2, on=['id','condition'], how='left')
df_combined3.drop(['sampling_count','simulation_time','sampling_resolution'], axis=1, inplace=True)
df_combined3.to_csv('CSV_Dataset\Combined\Combined_'+var+'_CS.csv', index=False)
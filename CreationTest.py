import pandas as pd
from sklearn import preprocessing
df1 = pd.read_csv('test.csv')
df  =  pd.read_csv('player_rates.csv')
df['DATE_R']=pd.to_datetime(df['DATE_R'])
df=df.loc[df.reset_index().groupby(['ID_P_R'])['DATE_R'].idxmax()]
df = df[['ID_P_R','POINT_R','POS_R']]
df1 =  df1.join(df.set_index('ID_P_R') , on = 'ID1_G' , rsuffix='_joueur1')
df1 =  df1.join(df.set_index('ID_P_R') , on = 'ID2_G' , rsuffix='_joueur2')
df = pd.read_csv('avestats2.csv')
df1 =  df1.join(df.set_index('ID1_G') , on = 'ID1_G' , rsuffix='_joueur1')
df1 =  df1.join(df.set_index('ID2_G') , on = 'ID2_G' , rsuffix='_joueur2')
values = {'POINT_R': 0, 'POINT_R_joueur2': 0, 'POS_R': 901, 'POS_R_joueur2': 901}
df1 = df1.fillna(value=values)
print(df1)
print("jgkjhl")
df = pd.read_csv('Processeddata/Tournois.csv',sep=';')
print(df.columns)
df1 =  df1.join(df.set_index('ID_T') , on = 'ID_T_G' , rsuffix='_T')
df1['PRIZE_T'] = df1['PRIZE_T'].convert_objects(convert_dates = False, convert_numeric= True, convert_timedeltas = False, copy = True)

df1 = df1.fillna(df1.mean())
L = ['POINT_R','POS_R', 'FS_1' , 'ACES_1' , 'DF_1' , 'W1S_1', 'W2S_1' , 'BP_1','POINT_R_joueur2','POS_R_joueur2', 'FS_1_joueur2' , 'ACES_1_joueur2' ,
     'DF_1_joueur2' , 'W1S_1_joueur2', 'W2S_1_joueur2' , 'BP_1_joueur2' ,'RANK_T' , 'PRIZE_T' , 'LATITUDE_T','LONGITUDE_T','TYPE_T_1','TYPE_T_2','TYPE_T_3','TYPE_T_4','TYPE_T_5','TYPE_T_6','ID_R_G']
df1 = df1[L]
df1.to_csv('merging_rank.csv',index= False)

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled= min_max_scaler.fit_transform(df1.values)

df2 = pd.DataFrame(x_scaled)
df2.columns = df1.columns

df2.to_csv('Processeddata/scaled_Test.csv', index = False)


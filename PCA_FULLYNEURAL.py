import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.read_csv('Processeddata/scaled_Train.csv',sep=";")
df = df.sample(frac= 1)
df2 = df.drop(['Resultat'], axis=1)
pca = PCA(n_components=6)
pca.fit(df2.values)
X = pca.transform(df2.values)
df2 = pd.DataFrame(X)
X = df2.values
df2['Resultat']=df['Resultat']
Y = df['Resultat'].values
df2.to_csv('Processeddata/ModelPCA_v2.csv', index = False)
print(' ===================================')
print(pca.explained_variance_ratio_)
print(' ===================================')
##############################################
n = len( X )//3


# fix random seed for reproducibility
seed = 7
np.random.seed(seed)


X_Train = X
Y_Train =Y
model = Sequential()
model.add(Dense(10, input_dim=6, activation='tanh'))
model.add(Dense(6, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_Train, Y_Train, epochs=10, batch_size=32)
Test_final = pd.read_csv('Processeddata/scaled_Test.csv',sep=",").values
X_Test =pca.transform(Test_final)
Result = model.predict(X_Test)
print(Result)
df = pd.read_csv('test.csv')
df['resultat']=re
df.to_csv('Resultat.csv')
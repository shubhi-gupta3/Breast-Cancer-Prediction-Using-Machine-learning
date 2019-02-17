import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
names=['id','clump thickness','uni of cell size','uni of cell shape',
       'marginal adhesion','cell size','bare nuclei','bland chromation',
       'normal nucleoli','mitoses','class']
data = pd.read_csv("db.data",names=names)
data.set_index('id', inplace=True)
pd.set_option('display.max_columns',None)
data['bare nuclei'].replace('?',np.nan,inplace=True)
data["bare nuclei"] = pd.to_numeric(data["bare nuclei"])
x=data.mean().astype(int)
data=data.fillna(x)
X=data.iloc[:,0:9]
X=X.values
y=data.iloc[:,9]
y=y.values
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.05)
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train,y_train)




test_new=[5,1,1,1,2,1,3,1,1]
out=knn.predict([test_new])
print(out)


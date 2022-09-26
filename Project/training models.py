from pyexpat.errors import XML_ERROR_UNEXPECTED_STATE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import seaborn as sns
rcParams['figure.figsize']=10,8
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

read_file = pd.read_excel ("/Users/samhitharao/Downloads/data (1).xlsx")

read_file.to_csv ("Test.csv",index = None,header=True)
df = pd.DataFrame(pd.read_csv("Test.csv"))

lm=LinearRegression()

x=df[['NO','CO','NO2','O3','NOx','T','AH','C6H6(GT)']]

y= df['RH']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33, random_state=42)

lm.fit(x_train,y_train)

prediction = lm.predict(x_test)

fig_dims = (6,3.5)
fig, ax = plt.subplots(figsize=fig_dims)
sns.scatterplot(y_test,prediction)

print('Accuracy of your prediction is',end=' ')
print(r2_score(y_test,prediction)*100,end='')
print('%')


from sklearn import metrics
from sklearn.metrics import recall_score
Regressor = LinearRegression()
prediction = lm.predict(x_test)
Regressor.fit(x_train,y_train)
print('MAE:', metrics.mean_absolute_error(y_test, prediction))
print('MSE:', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))
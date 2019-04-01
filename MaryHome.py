#simple analysis and regression on Maryalnd Home Performance Energy incentive program data
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

pd.set_option('display.expand_frame_repr', False) 
health = pd.read_csv('MarylandHomeAnalysis/MarylandHomeEnergy/Home_Performance_Energy_Efficiency_Projects_in_Maryland.csv')
print(health.columns)
health = health.drop('Program link:', axis=1)
health = health.drop('Location 1', axis=1)
new_cols = ['Program', 'County', 'Savings', 'Contribution','Cost']  #savings kwh, project cost $, MEA contribution $ 
health.columns = new_cols
print(health.shape)
print(health.head())
print(health.isna().any())

print(health['Program'].nunique())
print(health['County'].nunique())
print(health.describe())

print(len(health.loc[health['Contribution']==3100].index))      #number of entries w/ max MEA contribution
print(health.groupby('County').size().sort_values(ascending=False)) #entries by county

#simple visualizations
plt.scatter(x=health['Contribution'], y=health['Savings'])
plt.xlabel('MEA Contribution $')
plt.ylabel('Savings (kwh)')
plt.title('Savings vs. MEA Contribution')
plt.show()

plt.scatter(x=health['Cost'], y=health['Savings'])
plt.xlabel('Project Cost $')
plt.ylabel('Savings (kwh)')
plt.title('Savings vs. Project Cost')
plt.show()

plt.scatter(x=health['Cost'], y=health['Contribution'])
plt.xlabel('Project Cost $')
plt.ylabel('MEA Contribution $')
plt.title('MEA Contribution vs. Project Cost')
plt.show()


health = health.drop('Program', axis=1)
health = health.drop('County', axis=1)

target = np.array(health['Savings'])
health = health.drop('Savings', axis=1)
feats = np.array(health)

#fit model
X_train, X_test, y_train, y_test = train_test_split(feats, target, test_size = 0.25, random_state = 1748)
lr = LinearRegression(normalize = True)
reg = lr.fit(X = X_train, y=y_train)

#predictions and performance
preds = lr.predict(X_test)
MAE = mean_absolute_error(y_test, preds)
print('MAE: ',MAE)  #0.00022
MSE = mean_squared_error(y_test, preds)
print('MSE: ',MSE)  #7.449e-08
MAPE = np.mean(np.abs((y_test - preds)/y_test))*100
print('MAPE: '+ '{:.2%}'.format(MAPE))  #0.89%
print('r2 Score: ',r2_score(y_test, preds)) #0.9999

coef_dict = {}
for coef, feat in zip(lr.coef_, health.columns):
    coef_dict[feat] = coef 

print('Contribution: ',coef_dict['Contribution'])
print('Cost: ',coef_dict['Cost'])


import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt


'''
# SYKSY = Syys-, loka- ja marraskuu ovat syksyn kuukausia
# TALVI = Joulu-, tammi- ja helmikuu ovat talven kuukaudet.
# KEVAT = Kevatkuukaudet ovat maalis-, huhti- ja toukokuu.
# KESA =  Kesa-, heina- ja elokuu ovat kesan kuukaudet.
'''



df = pd.read_csv('2018_values.csv', index_col=0)
df.index = pd.to_datetime(df.index)
df = df.sort_index()

talvi_1 = df.loc['2018-01-01':'2018-02-28']
talvi_2 = df.loc['2018-12-01':'2018-12-31']
kevat = df.loc['2018-03-01':'2018-05-31']
kesa = df.loc['2018-06-01':'2018-08-31']
syksy = df.loc['2018-09-01':'2018-11-30']
talvi_df = []

talvi_df.append(talvi_1)
talvi_df.append(talvi_2)

talvi = pd.concat(talvi_df, ignore_index=False, axis=0)

df['Delay'] = df['Delay'].astype(float)

talvi_data = talvi.values
kevat_data = kevat.values
kesa_data = kesa.values
syksy_data = syksy.values

year_data = [talvi_data, kevat_data, kesa_data, syksy_data]

#TODO: Predict whether Delay will be below 2 minutes? Probability of over 2 minute delay?
# Planned arrival time is 15:56, with a 2 minutes walk from train station to basketball game would be 15:58 arrival at basketball game
# Therefore, the train can be late in arriving Tampere only 2 minutes !!! 15:58 + 2 mins = 16:00



# TODO: Start of ARIMA based linear modelling, to be completed.

df_stocks = df.iloc[:180] #first 180 points ere used to fit the model. Next 180 are used as validation set
df_holdout = df.iloc[180:] #Validation or holdout set
df_stocks.plot()

df_stocks_diff = df_stocks-df_stocks.shift() #To remove the trend and achieve stationarity, we plot the differenced time series
df_stocks_diff.plot()

model = ARIMA(df_stocks, order=(2,1,1))
results_AR = model.fit(disp=-1)

#plt.show()


predictions_AR = results_AR.predict(start=len(df_stocks_diff),end=len(df_stocks_diff)+180)
predictions_AR.iloc[0] = predictions_AR.iloc[0]+df_stocks.iloc[178]
predictions_AR = predictions_AR.cumsum()
predictions_AR.head()

predictions_AR.index = df_holdout.index


plt.plot(df_stocks)
plt.plot(df_holdout)
plt.plot(predictions_AR)

error = mean_squared_error(df_holdout, predictions_AR)
print(error)
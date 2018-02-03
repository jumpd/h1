#Using a Deep Neural Net to Predict Performance of NBA Players based on
#social media from kaggle dataset found here-->

import pandas as pd


data_set_path = 'nba_2016_2017_100.csv'
nba_data = pd.read_csv(data_set_path)
print(nba_data.shape)
print(nba_data.columns)

#we will only use numeric data features (but can one-hot encode)
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
nba_df = nba_data.select_dtypes(include=numerics)
print(nba_df.columns)



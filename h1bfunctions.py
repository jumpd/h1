import pandas as pd
import matplotlib.pyplot as plt

def get_data(path_to_data, chunk='all'):
    '''
    This function extracts the data from csv file to pandas dataframe
    '''
    if chunk == 'all':
        dwdata = pd.read_csv(path_to_data)
    else:
        dwdata = pd.read_csv(path_to_data, nrows = chunk)
    return Xset, Yset

def format_clean(data):
    '''
    This function does some basic transformation on data
    We want to remove the 'Withdrawn' from the target labeled dataset 
    and meger 'Certified-Withdrawn' with 'Certified' in 
    order to make the y_labels/targets binary 
    '''
    
    df1 = data.drop('Withdrawn', axis=0)
    
    return cleaned


def visualize(data):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    num_df = xs.select_dtypes(include=numerics)
    pd.scatter_matrix(num_df)
    plt.show()



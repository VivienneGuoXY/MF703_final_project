import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test(a):
    return a*np.random.rand()

def get_first_n_date(filename,n=100):
    df = pd.read_csv(filename)
    return df['Date'][:n]

def get_first_n_close(filename,n=100):
    df = pd.read_csv(filename)
    return df['Adj Close'][:n]

def plot_date_close(date,close):
    plt.plot(date,close)
    plt.xlabel('Date')
    plt.ylabel('Adj Close')
    plt.show()
    
if __name__ == '__main__':
    #print(test(100))
    filename = 'AAPL.csv'
    #n = 200
    date = get_first_n_date(filename)
    close = get_first_n_close(filename)
    plot_date_close(date,close)
import pandas as pd

if __name__ == '__main__':

    df = pd.read_csv('books.csv')
    print(df.head())

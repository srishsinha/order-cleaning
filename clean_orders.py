import pandas as pd

df = pd.read_csv('orders.csv')

cleaned_df = df[df['amount']!=0]

cleaned_df.to_csv('cleaned_orders.csv', index = False)
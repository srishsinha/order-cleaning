import pandas as pd

df = pd.read_csv('orders.csv')

cleaned_df = df[df['amount']!=0]

cleaned_df.to_csv('cleaned_orders.csv', index = False)

total_amount = cleaned_df['amount'].sum()
print(f"Total amount of cleaned orders: {total_amount}")
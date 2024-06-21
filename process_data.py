import pandas as pd

def process_data(file_path):
    df = pd.read_csv(file_path)
    df_sorted = df.sort_values(by='Price', ascending=False)
    df_sorted.to_csv('zillow_recently_sold_sorted.csv', index=False)
    df_sorted.to_excel('zillow_recently_sold_sorted.xlsx', index=False)
    df_sorted.to_json('zillow_recently_sold_sorted.json', orient='records', lines=True)
    return df_sorted

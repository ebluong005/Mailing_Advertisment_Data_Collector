import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(file_path):
    df = pd.read_csv(file_path)
    top_10 = df.head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top_10['Address'], top_10['Price'], color='skyblue')
    plt.xlabel('Price ($)')
    plt.title('Top 10 Most Expensive Houses Recently Sold')
    plt.gca().invert_yaxis()
    plt.savefig('top_10_expensive_houses.png')
    plt.show()

import pandas as pd

def generate_mailing_list(file_path):
    df = pd.read_csv(file_path)
    addresses = df['Address']
    prices = df['Price']
    mailing_list = "\n".join([f"{address} - ${price}" for address, price in zip(addresses, prices)])

    with open('mailing_list.txt', 'w') as file:
        file.write(mailing_list)

    print("Mailing list saved to mailing_list.txt")

if __name__ == "__main__":
    generate_mailing_list('zillow_recently_sold_sorted.csv')

import requests
from bs4 import BeautifulSoup
import pandas as pd
from utils import log_message, send_email

# URL of the Zillow page to scrape (modify with the appropriate search query)
url = 'https://www.zillow.com/homes/recently_sold/'

# Headers to mimic a browser visit (important to avoid being blocked)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_data():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        house_elements = soup.find_all('article', {'class': 'list-card'})

        houses = []
        for house in house_elements:
            address = house.find('address', {'class': 'list-card-addr'}).text
            price = house.find('div', {'class': 'list-card-price'}).text
            status = house.find('div', {'class': 'list-card-statusText'}).text
            date_sold = house.find('div', {'class': 'list-card-variableText'}).text if house.find('div', {'class': 'list-card-variableText'}) else 'N/A'
            details = house.find('ul', {'class': 'list-card-details'})
            bedrooms = details.find_all('li')[0].text if details and len(details.find_all('li')) > 0 else 'N/A'
            bathrooms = details.find_all('li')[1].text if details and len(details.find_all('li')) > 1 else 'N/A'
            area = details.find_all('li')[2].text if details and len(details.find_all('li')) > 2 else 'N/A'
            price_num = int(price.replace('$', '').replace(',', ''))

            houses.append({
                'Address': address,
                'Price': price_num,
                'Status': status,
                'Date Sold': date_sold,
                'Bedrooms': bedrooms,
                'Bathrooms': bathrooms,
                'Area': area
            })

        df = pd.DataFrame(houses)
        df_sorted = df.sort_values(by='Price', ascending=False)
        df_sorted.to_csv('zillow_recently_sold_sorted.csv', index=False)
        df_sorted.to_excel('zillow_recently_sold_sorted.xlsx', index=False)
        df_sorted.to_json('zillow_recently_sold_sorted.json', orient='records', lines=True)
        
        log_message('Scraping and saving data completed successfully.')
        send_email('Zillow Scraper Update', 'The scraping process has been completed and the data has been updated.')

        return df_sorted
    else:
        log_message(f'Failed to retrieve the webpage. Status code: {response.status_code}')
        return None

if __name__ == "__main__":
    scrape_data()

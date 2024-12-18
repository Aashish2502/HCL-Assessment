from bs4 import BeautifulSoup
import pandas as pd

with open('main.html', 'r') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
prod_names = soup.find_all('h2')
prod_names = [name.getText()[14:] for name in prod_names]
prod_prices = soup.find_all(class_="price")
prod_prices = [price.getText()[10:] for price in prod_prices]
prod_prices

df = pd.DataFrame({'Product Name': prod_names, 'Product Price (In Rs.)': prod_prices})
print(df)
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

soup.find('table')

soup.find_all('table')[1]

print(table)

world_titles = table.find_all('th')

world_titles

world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


import pandas as pd

df = pd.DataFrame(columns = world_table_titles)

df

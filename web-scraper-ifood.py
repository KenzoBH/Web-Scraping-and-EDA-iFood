# ----------------------------------------------------
#
# This program is a Web Scraping proccess to get data
# from IFood website, for future analysis
# (the comments in this code are in English).
# - Bruno Kenzo, http://kenzobh.github.io.
#
# ----------------------------------------------------

import pandas as pd # Data manipulation and DataFrame creation
from selenium.webdriver import Chrome, ChromeOptions # For Web Scraping
import time

browser = Chrome(executable_path = 'ADD-YOUR-chromedriver.exe-PATH')

n_scrolls = 8 # Number of scrolls in the page, to get more data

# Open the iFood page: it will search for restaurants in a 10km distance radius
ifood_url = 'https://www.ifood.com.br/lista-restaurantes?f_distance=10'
browser.get(ifood_url)

# Clicks on "Usar minha localização" button
# <button class="btn-address--full-size" aria-label="Usar minha localização">
use_my_location_button = browser.find_element_by_xpath('//button[@class="btn-address--full-size"]')
use_my_location_button.click()
time.sleep(3)

# Clicks on "Ver mais restaurantes e mercados" button "n_scrolls" times
# <button type="button" role="button" class="btn btn--default btn--white btn--size-m btn--full-width restaurants-list__load-more" aria-label="Ver mais restaurantes e mercados" color="white" variant="restaurants-list__load-more" theme="default" target="" rel="">
for _ in range(n_scrolls): # Scrolls the page 'n_scrolls' times, to get more restaurants
    browser.execute_script("window.scrollTo(0, document);")
    time.sleep(3)
    load_more_button = browser.find_element_by_xpath('//button[@class="btn btn--default btn--white btn--size-m btn--full-width restaurants-list__load-more"]')
    load_more_button.click()
    time.sleep(3)

# Get the restauraurant name
# <span class="restaurant-name">
restaurants = [rest.text for rest in browser.find_elements_by_xpath('//span[@class="restaurant-name"]')]
# print(restaurants)
# print(len(restaurants))

# Get the rate, the food type and the distance from me
# <div class="restaurant-card__info">
some_info = [info.text for info in browser.find_elements_by_xpath('//div[@class="restaurant-card__info"]')]
# print(some_info) # Element example: '4.9\n•\nLanches\n•\n3,6 km'
# print(len(some_info))
ratings = []
types = []
distances = []
for i in some_info: # The data comes dirty: '4.9\n•\nLanches\n•\n3,6 km', then we have to split the elements of the list
    ratings.append(float(i.split('\n•\n')[0]))
    types.append(i.split('\n•\n')[1])
    distances.append(float(i.split('\n•\n')[2][:-3].replace(',', '.')))

# Get the time distance and the greight price from each restaurant
# <div class="restaurant-card__footer">
times_and_freight_prices = [info.text for info in browser.find_elements_by_xpath('//div[@class="restaurant-card__footer"]')]
# print(times_and_freight_prices)
# print(len(times_and_freight_prices)) # Element example: '66-76 min\n•\nR$ 2,99'
times = []
freight_prices = []
for i in times_and_freight_prices: # The data comes dirty here too
    times.append(i.split('\n•\n')[0])
    if i.split('\n•\n')[1] == 'Grátis':
        freight_prices.append(0)
    else:
        freight_prices.append(float(i.split('\n•\n')[1][3:].replace(',', '.')))

# Creates a Dataframe and saves in a csv file
df = pd.DataFrame({'Restaurante': restaurants,
                   'Nota': ratings,
                   'Tipo de comida': types,
                   'Distancia': distances,
                   'Tempo': times,
                   'Preco do Frete': freight_prices})
df.to_csv('dados-ifood.csv') # Clean data!
print(df)

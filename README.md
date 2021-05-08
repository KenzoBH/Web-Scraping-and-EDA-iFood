# iFood!
This project is about collect data from [iFood website](https://www.ifood.com.br/lista-restaurantes) and explore it.   
It was developed with IME Jr. - Junior Enterprise from Maths and Statistics Institute from University of São Paulo - team members.

## [The Web Scraper](https://github.com/KenzoBH/Web-Scraping-and-EDA-iFood/blob/main/web-scraper-ifood.py)
The Web Scraper was developed in Python, using [Selenium](https://www.selenium.dev/) and [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html).   
Was scraped data from +100 restaurants next to me, in a radius of 10km.    

## [The Scraped Data](https://github.com/KenzoBH/Web-Scraping-and-EDA-iFood/blob/main/scraped-data.csv)
The scraped data from iFood website is stored in a `.csv` file. You can download it if you want. Or scrape some data yourself, with the [web scraper](https://github.com/KenzoBH/Web-Scraping-and-EDA-iFood/blob/main/web-scraper-ifood.py) above, inputing your data in the program, using your PC location.   
These are the first 5 rows of the data frame:

| Restaurante | Nota | Tipo de comida | Distancia | Tempo | Preco do Frete |
| ----------- | ---- | -------------- | --------- | ----- | -------------- |
|Gokei - Carrão|4.6|Japonesa|0.9|59-69 min|0.0|
|Pikurruchas Tatuapé|4.7|Doces & Bolos|2.3|34-44 min|6.99|
|Mussa Esfiha - Anália Franco|4.7|Árabe|2.1|23-33 min|7.99|
|Sassá Sushi - Tatuapé|4.4|Japonesa|3.8|41-51 min|10.49|
|Meats - Anália Franco|4.7|Lanches|2.6|22-32 min|6.99|

## [Cleaning Some Data](https://github.com/KenzoBH/Web-Scraping-and-EDA-iFood/blob/main/cleaning-data.ipynb)
As this project was developed with the IME Jr. team, each member scraped its own data. This Jupyter Notebook (`.ipynb`) is about cleaning and joining 4 different dataframes from the team. The final file is [here](https://github.com/KenzoBH/Web-Scraping-and-EDA-iFood/blob/main/final-ifood-data.csv), (`final-ifood-data.csv`).

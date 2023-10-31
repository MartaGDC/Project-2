import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

import src.downloading_and_cleaning as clean
import src.scrapping as scrap
import src.visualizing as vis


df_amazon = clean.importarCsv("data/bestsellers_with_categories_2022_03_27.csv")
amazon_csv = clean.cleanAmazon(df_amazon)
clean.saveCsv(amazon_csv, "amazon")

df_spanish = clean.importarCsv("data/libros_mas_vendidos.csv")
spanish_csv = clean.cleanSpanish(df_spanish)
clean.saveCsv(spanish_csv, "spanish")


urls = scrap.getUrls("https://www.todostuslibros.com/mas_vendidos")
bodies = [scrap.getBodies(i) for i in urls]
links_secondary = [scrap.getLinks(i) for i in bodies]
titles_df = scrap.getTitles_df(bodies)
authors_df = scrap.getAuthors_df(bodies)
genres_df = scrap.getGenres_df(links_secondary)
editorials_df = scrap.getEditorials_df(links_secondary)
countries_df = scrap.getCountries_df(links_secondary)
languages_df = scrap.getLanguages_df(links_secondary)
orig_lang_df = scrap.getOrigLang_df(links_secondary)
pages_df = scrap.getPages_df(links_secondary)
dates_df = scrap.getDates_df(links_secondary)
prices_df = scrap.getPrices_df(bodies)
df_web = scrap.build_df(titles_df, authors_df, genres_df, editorials_df, countries_df, languages_df, orig_lang_df, pages_df, dates_df, prices_df)
scrap.cleaning_Web(df_web)

vis.amazonGenres("data/amazon_projectII.csv")
vis.amazonGenresYear("data/amazon_projectII.csv")
vis.amazonPrices("data/amazon_projectII.csv")
vis.amazonPricesYear("data/amazon_projectII.csv")
vis.amazonTopGenresYear("data/amazon_projectII.csv")
vis.dbBookshopGenres("data/spanish_projectII.csv")
vis.dbBookshopTopGenres("data/spanish_projectII.csv")
vis.dbBookshopEditorials("data/spanish_projectII.csv")
vis.dbBookshopForeign("data/spanish_projectII.csv")
vis.webBookshopGenres("data/web_projectII.csv")
vis.webPrices("data/web_projectII.csv")
vis.webBookshopTopGenres("data/web_projectII.csv")
vis.webBookshopEditorials("data/web_projectII.csv")
vis.webBookshopForeign("data/web_projectII.csv")
vis.bookshops("data/spanish_projectII.cs", "data/web_projectII.csv")

vis.shopGenres("data/shops_projectII.csv")

vis.shopGenresYear("data/shops_projectII.csv")
vis.shopTopGenresYear("data/shops_projectII.csv")
vis.shopForeign("data/shops_projectII.csv")

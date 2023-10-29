# Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


url_basal = "https://www.todostuslibros.com/mas_vendidos"


# Functions to retrieve items from one page:
def getBodies(url):
    res = requests.get(url)
    html = res.content
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find("main", {"class": "main"})
    return body
def getTitles(body):
    titles_info = body.find_all("li", {"class":"book row"})
    titles = [titles_info[i].get("data-gtm-titulo") for i in range(len(titles_info))]
    return titles
def getAuthors(body):
    authors_info = body.find_all("li", {"class":"book row"})
    authors = [authors_info[i].find_all("h3", {"class":"author"})[0].getText().strip() for i in range(len(authors_info))]
    return authors
def getLinks(body):
    link_info = body.find_all("div", {"class": "book-image col-4 col-sm-3 col-md-3 col-lg-3"})
    link_unpross = [link_info[i].find_all("a") for i in range(len(link_info))]
    links = [link_unpross[i][0].get("href") for i in range(len(link_info))]
    return links
def getGenres(links):
    genres = []
    for i in links:
        url = i
        res = requests.get(url)
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        genres_unpross = soup.find_all("dl", {"class":"materias"})[0].getText().strip().split("\n")[1:]
        genre_for_each_title = [i.strip() for i in genres_unpross if "|" not in i][1:]
        genres.append(genre_for_each_title)
    return genres
def getEditorials(links):
    editorials = []
    for i in links:
        url = i
        res = requests.get(url)
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        editorials_unpross = soup.find_all("div", {"id":"collapseFic"})[0].find("a").getText()
        editorials.append(editorials_unpross)
    return editorials
def getCountries(links):
    countries = []
    for i in links:
        url = i
        res = requests.get(url)
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        countries_unpross = soup.find_all("div", {"id":"collapseFic"})[0].find_all("dd")[-8].getText()
        countries.append(countries_unpross)
    return countries
def getLanguages(links):
    languages = []
    for i in links:
        url = i
        res = requests.get(url)
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        languages_unpross = soup.find_all("div", {"id":"collapseFic"})[0].find_all("dd")[-7].getText()
        languages.append(languages_unpross)
    return languages
def getLang_orig(links):
    orig_language = []
    for i in links:
        url = i
        res = requests.get(url)
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        orig_language_unpross = soup.find_all("div", {"id":"collapseFic"})[0].find_all("dd")[-6].getText()
        orig_language.append(orig_language_unpross)
    return orig_language
def getPages(links):
    pages = []
    for i in links:
        url = i
        res = requests.get(url)
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        pages_unpross = soup.find_all("div", {"id":"collapseFic"})[0].find_all("dd")[-3].getText()
        pages.append(pages_unpross)
    return pages
def getDates(links):
    fechas = []
    for i in links:
        url = i
        res = requests.get(url)
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        fechas_unpross = soup.find_all("div", {"id":"collapseFic"})[0].find_all("dd")[-2].getText()
        fechas.append(fechas_unpross)
    return fechas
def getPrices(body):
    prices_info = body.find_all("div", {"class":"book-price d-block d-md-none"})
    prices = [prices_info[i].find("strong").getText().strip() for i in range(len(prices_info))]
    return prices

# Functions to retrieve items from several pages:
def getUrls():
    urls = [(url_basal + "?page=" + str(i)) for i in range(1, 11)]
    return urls

urls = getUrls()
bodies = [getBodies(i) for i in urls]
links_secondary = [getLinks(i) for i in bodies]

def getTitles_df(bodies):
    titles_100 = []
    for i in bodies:
        titles = getTitles(i)
        titles_100.extend(titles)
    return titles_100
def getAuthors_df(bodies):
    authors_100 = []
    for i in bodies:
        authors = getAuthors(i)
        authors_100.extend(authors)
    return authors_100
def getGenres_df(links_secondary):
    genres_100 = []
    for i in links_secondary:
        genres = getGenres(i)
        genres_100.extend(genres)
    return genres_100
def getEditorials_df(links_secondary):
    editorials_100 = []
    for i in links_secondary:
        editorials = getEditorials(i)
        editorials_100.extend(editorials)
    return editorials_100
def getCountries_df(links_secondary):
    countries_100 = []
    for i in links_secondary:
        countries = getCountries(i)
        countries_100.extend(countries)
    return countries_100
def getLanguages_df(links_secondary):
    languages_100 = []
    for i in links_secondary:
        languages = getLanguages(i)
        languages_100.extend(languages)
    return languages_100
def getOrigLang_df(links_secondary):
    orig_lang_100 = []
    for i in links_secondary:
        orig_lang = getLang_orig(i)
        orig_lang_100.extend(orig_lang)
    return orig_lang_100
def getPages_df(links_secondary):
    pages_100 = []
    for i in links_secondary:
        pages = getPages(i)
        pages_100.extend(pages)
    return pages_100
def getDates_df(links_secondary):
    dates_100 = []
    for i in links_secondary:
        dates = getDates(i)
        dates_100.extend(dates)
    return dates_100
def getPrices_df(bodies):
    prices_100 = []
    for i in bodies:
        prices = getPrices(i)
        prices_100.extend(prices)
    return prices_100

titles_df = getTitles_df(bodies)
authors_df = getAuthors_df(bodies)
genres_df = getGenres_df(links_secondary)
editorials_df = getEditorials_df(links_secondary)
countries_df = getCountries_df(links_secondary)
languages_df = getLanguages_df(links_secondary)
orig_lang_df = getOrigLang_df(links_secondary)
pages_df = getPages_df(links_secondary)
dates_df = getDates_df(links_secondary)
prices_df = getPrices_df(bodies)

# Function to save a csv after scrapping
def build_df(titles_df, authors_df, genres_df, editorials_df, countries_df, languages_df, orig_lang_df, pages_df, dates_df, prices_df):
    dictionary = {
        "titles":titles_df,
        "authors":authors_df,
        "genres": genres_df,
        "editorial":editorials_df,
        "countries":countries_df,
        "languages":languages_df,
        "orig_language": orig_lang_df,
        "pages":pages_df,
        "dates":dates_df,
        "prices": prices_df
    }
    library_csv = pd.DataFrame(dictionary)
    library_csv.to_csv("../data/web_projectII.csv", index=False)

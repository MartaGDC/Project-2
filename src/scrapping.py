# Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


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
def getUrls(url_basal):
    urls = [(url_basal + "?page=" + str(i)) for i in range(1, 11)]
    return urls

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


# Function to create a df after scrapping
def build_df(titles_df, authors_df, genres_df, editorials_df, countries_df, languages_df, orig_lang_df, pages_df, dates_df, prices_df):
    dictionary = {
        "title":titles_df,
        "author":authors_df,
        "genre": genres_df,
        "editorial":editorials_df,
        "country":countries_df,
        "language":languages_df,
        "orig_language": orig_lang_df,
        "pages":pages_df,
        "date":dates_df,
        "price": prices_df
    }
    return pd.DataFrame(dictionary)

# Cleaning
def cleaning_Web(df):
    lst_fiction = ["['Género policíaco y misterio', 'Obra de espionaje y espías']",
                   "['Ficción histórica', 'Obra de misterio y suspense', 'Ficción moderna y contemporanea']",
                   "['Ficción de las guerras napoleónicas', 'Ficción histórica']", "['Ficción moderna y contemporanea']",
                   "['Islas griegas', 'Ficción moderna y contemporanea', 'Género policíaco y misterio']",
                   "['HUMOR', 'Edad de interés: a partir de 10 años', 'Cómics y novelas gráficas']",
                   "['Ficción histórica', 'Nueva York', 'Ficción moderna y contemporanea']",
                   "['Ficción moderna y contemporanea']", "['Ficción moderna y contemporanea']",
                   "['Perú', 'Música del mundo', 'Ficción moderna y contemporanea']",
                   "['Noruega', 'Ficción moderna y contemporanea']",
                   "['Edad de interés: a partir de 12 años', 'Cuestiones personales y sociales: autoconocimiento y autoestima (infantil/juvenil)', 'Ficción general (infantil/juvenil)']",
                   "['Fantasía']", "['Cuentos de terror y fantasmas', 'Obra de misterio y suspense']", "['Novelas gráficas']",
                   "['Género policíaco y misterio']",
                   "['Narrativa romántica', 'Ficción erótica', 'Ficción moderna y contemporanea', 'Edad de interés: a partir de 14 años', 'Ficción general (infantil/juvenil)']",
                   "['Ficción moderna y contemporanea']", "['Ficción histórica']", "['Ficción moderna y contemporanea']",
                   "['Relatos sobre la escuela (infantil/juvenil)', 'Caricaturas e historietas (infantil/juvenil)', 'Relatos de humor (infantil/juvenil)']",
                   "['Noruega', 'Europa del Norte, Escandinavia', 'Narrativa romántica adulta y contemporánea', 'Obra de misterio y suspense', 'Ficción moderna y contemporanea', 'EUROPA', 'Literatura y estudios literarios']",
                   "['Edad de interés: a partir de 10 años', 'Cuestiones personales y sociales: autoconocimiento y autoestima (infantil/juvenil)', 'Ficción clásica (infantil/juvenil)']",
                   "['Autobiografía: general', 'Ficción moderna y contemporanea']",
                   "['Obra de misterio y suspense', 'Género policíaco y misterio']",
                   "['Patinaje sobre hielo', 'Narrativa romántica adulta y contemporánea']",
                   "['Islas Baleares, Comunidad Autónoma de', 'Ficción moderna y contemporanea']",
                   "['Ficción moderna y contemporanea']", "['Género policíaco y misterio']",
                   "['Relatos románticos y de relaciones interpersonales (infantil/juvenil)', 'Edad de interés: a partir de 14 años', 'Fantasía y realismo mágico (infantil/juvenil)']",
                   "['Japón', 'Cocina nacional y regional', 'Género policíaco y misterio']",
                   "['Fantasía', 'MITOS Y LEYENDAS NARRADOS COMO FICCIÓN', 'Ficción moderna y contemporanea']",
                   "['Ficción histórica', 'Inglaterra', 'Ficción moderna y contemporanea']",
                   "['Cómics y novelas gráficas', 'Edad de interés: a partir de 8 años', 'Novelas gráficas: manga']",
                   "['Madrid, Comunidad de', 'Ficción moderna y contemporanea']",
                   "['Relatos románticos y de relaciones interpersonales (infantil/juvenil)']", "['Ficción moderna y contemporanea']",
                   "['Italia', 'Ficción moderna y contemporanea']",  "['Ficción moderna y contemporanea']",
                   "['Historia: acontecimientos y temas específicos', 'Historia del siglo xxi: c. 2000-', 'Ficción moderna y contemporanea']",
                   "['Misterios, lo sobrenatural, monstruos y seres mitológicos (infantil/juvenil)', 'Ficción de crimen y misterio (infantil/juvenil)', 'Relatos de aventuras (infantil/juvenil)', 'Edad de interés: a partir de 6 años', 'Dinosaurios y el mundo prehistórico (infantil/juvenil)']",
                   "['Siglo xx', 'Ficción moderna y contemporanea', 'Sagas']", "['FICCIÓN E HISTORIAS REALES INFANTILES Y JUVENILES']",
                   "['FICCIÓN E HISTORIAS REALES INFANTILES Y JUVENILES', 'España', 'Español / Castellano', 'Edad de interés: a partir de 14 años']",
                   "['Género policíaco y misterio', 'Ficción moderna y contemporanea', 'Obra de misterio y suspense']",
                   "['Edad de interés: a partir de 8 años', 'Thriller (infantil/juvenil)', 'Fantasía y realismo mágico (infantil/juvenil)']",
                   "['Ficción moderna y contemporanea']", "['Novela gráfica y manga como obra de arte', 'Novelas gráficas']",
                   "['Ficción general (infantil/juvenil)', 'Relatos de humor (infantil/juvenil)', 'Relatos de aventuras (infantil/juvenil)']",
                   "['Ficción moderna y contemporanea', 'Aventura histórica', 'Misterios históricos']",
                   "['Obra de suspense político y judicial']", "['Novelas gráficas']",
                   "['Obra de misterio y suspense', 'Género policíaco y misterio', 'Ficción moderna y contemporanea', 'Obra de suspense político y judicial']",
                   "['c. 1960\\x96c. 1970', 'Estados Unidos de América', 'Ficción moderna y contemporanea']",
                   "['Fantasía romántica (juvenil)', 'Ficción general (infantil/juvenil)', 'Edad de interés: a partir de 14 años', 'Ficción moderna y contemporanea']",
                   "['Ficción clásica']", "['Ficción moderna y contemporanea']",
                   "['Italia', 'Irlanda', 'Ficción moderna y contemporanea']",
                   "['FICCIÓN E HISTORIAS REALES INFANTILES Y JUVENILES', 'España', 'Español / Castellano', 'Edad de interés: a partir de 12 años']",
                   "['Ficción moderna y contemporanea']", "['Género policíaco y misterio']",
                   "['Sagas', 'Narrativa romántica histórica']",
                   "['Español / Castellano', 'Francia', 'Ficción moderna y contemporanea']",
                   "['Edad de interés: a partir de 6 años', 'Cuentos tradicionales', 'Relatos de aventuras (infantil/juvenil)']",
                   "['Obra de misterio y suspense', 'Género policíaco y misterio', 'Ficción moderna y contemporanea']",
                   "['Ficción moderna y contemporanea', 'Ficción y temas afines', 'Cuentos de terror y fantasmas']",
                   "['Ficción moderna y contemporanea']"]

    lst_nofiction = ["['Religión y creencias']",
                    "['Mente, cuerpo y espíritu: pensamiento y práctica', 'Afirmación personal, motivación y autoestima', 'APLICACIONES EMPRESARIALES', 'Estrategias y políticas educativas', 'Autoayuda y desarrollo personal']",
                    "['Francia', 'CIENCIA: CUESTIONES GENERALES']",
                    "['Música: estilos y géneros', 'Actores e intérpretes', 'Autobiografía: arte y espectáculo']",
                    "['Estudios generales']", "['Autoayuda y desarrollo personal']", "['Estudios generales']",
                    "['Anuarios, almanaques, publicaciones anuales']",
                    "['Divulgación científica', 'Invenciones e inventores', 'Crímenes reales: descubrimientos/históricas/científicas']",
                    "['Prosa: no ficción']", "['Autoayuda y desarrollo personal']",
                    "['Autoayuda y desarrollo personal', 'Afirmación personal, motivación y autoestima']",
                    "['Afirmación personal, motivación y autoestima', 'Mente, cuerpo y espíritu: meditación y visualización']",
                    "['Mente, cuerpo y espíritu: pensamiento y práctica']",
                    "['Historia social y cultural', 'Historia: acontecimientos y temas específicos', 'c. 1700-c. 1800', 'Revoluciones, levantamientos y rebeliones']",
                    "['El Holocausto', 'Psicoterapia', 'c. 1939-c. 1945 (incluye la Segunda Guerra Mundial)', 'Español / Castellano', 'Psicología']",
                    "['Antigua Roma', 'Historia antigua: hasta c. 500 e. c.']",
                    "['Violencia en la sociedad', 'Comunidades rurales', 'Cuestiones y procesos sociales']",
                    "['Biografía: literaria', 'Biografía: general', 'Biografía e historias relaes', 'Asia Oriental, Lejano Oriente', 'Literatura de viajes']",
                    "['Finanzas personales', 'Economía']", "['Psicoterapia']", "['Historia']", "['Medicina popular y salud']",
                    "['Cuestiones personales y sociales: autoconocimiento y autoestima (infantil/juvenil)', 'Edad de interés: a partir de 3 años', 'Álbumes ilustrados']",
                    "['Autoayuda y desarrollo personal', 'Poesía', 'Afirmación personal, motivación y autoestima']",
                    "['Reportajes y colección de artículos periodísticos']", "['Dietética y nutrición', 'Dietas y régimen alimenticio']",
                    "['Cuestiones personales y sociales: sexualidad y relaciones interpersonales (infantil/juvenil)', 'Cuestiones personales y sociales: cuerpo y salud (infantil/juvenil)', 'Álbumes ilustrados']",
                    "['Fenómenos inexplicables/paranormales', 'Ovnis y seres extraterrestres']",
                    "['Política y Gobierno', 'Historia']",
                    "['Halloween', 'ARTÍCULOS DE ESCRITORIO INFANTILES Y VARIOS', 'Aprendizaje temprano/conceptos de aprendizaje temprano', 'Libros y paquetes interactivos y de actividades', 'Álbumes ilustrados', 'Para niños c. 0-2 años', 'Libros para bebés']",
                    "['Astrología', 'Jardinería', 'Agricultura orgánica', 'Horticultura', 'AGRICULTURA Y EXPLOTACIÓN AGROPECUARIA']"]
    def clasif(x):
        if x["genre"] in lst_fiction:
            return "fiction"
        elif x["genre"] in lst_nofiction:
            return "non-fiction"
        else:
            return None
    df["genres_clasif"] = df.apply(clasif, axis=1)
    df["price"] = df["price"].str.extract("(.{1,6})€")
    df["price"] = pd.to_numeric(df["price"])
    df.loc[4,"orig_language"] = "Francés"
    df.loc[68,"orig_language"] = "Castellano"
    df.loc[34,"orig_language"] = "Noruego"
    df.to_csv("data/web_projectII.csv", index=False)

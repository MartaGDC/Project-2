# Libraries
import pandas as pd

def importarCsv(path):
    return pd.read_csv(path)

def cleanAmazon(df):
    book_csv = df.drop_duplicates(subset=['Name', 'Year'])
    book_csv.columns = [i.lower() for i in book_csv.columns]
    book_csv.rename({"name":"title"}, axis = 1, inplace = True)
    book_csv.rename({"year":"year_bought"}, axis = 1, inplace = True)
    book_csv.drop(book_csv["year_bought"][book_csv["year_bought"]< 2020].index, axis = 0, inplace = True)
    book_csv.sort_values(by = "reviews", ascending = False, inplace=True)
    book_csv.reset_index(inplace = True)
    book_csv.drop(["user rating", "reviews", "index"], axis = 1, inplace = True)
    return book_csv

def cleanSpanish(df):
    books_csv = df.drop(["Url", "Traductor", "Colección", "Encuadernación", "ISBN", "EAN", "Dimensiones", "Peso", "Ilustrador"], axis = 1)
    books_csv.rename({"Puesto":"order"}, axis = 1, inplace = True)
    books_csv.rename({"Título":"titles"}, axis = 1, inplace = True)
    books_csv.rename({"Autor":"authors"}, axis = 1, inplace = True)
    books_csv.rename({"Materias":"genres"}, axis = 1, inplace = True)
    books_csv.rename({"Editorial":"editorial"}, axis = 1, inplace = True)
    books_csv.rename({"País de publicación ":"countries"}, axis = 1, inplace = True)
    books_csv.rename({"Idioma de publicación ":"languages"}, axis = 1, inplace = True)
    books_csv.rename({"Idioma original ":"orig_language"}, axis = 1, inplace = True)
    books_csv.rename({"Nº páginas":"pages"}, axis = 1, inplace = True)
    books_csv.rename({"Fecha publicación ":"dates"}, axis = 1, inplace = True)
    return books_csv

def saveCsv(df, name):
    df.to_csv(f"data/{name}_projectII.csv", index=False)


df_amazon = importarCsv("data/bestsellers_with_categories_2022_03_27.csv")
amazon_csv = cleanAmazon(df_amazon)
saveCsv(amazon_csv, "amazon")

df_spanish = importarCsv("data/libros_mas_vendidos.csv")
spanish_csv = cleanSpanish(df_spanish)
saveCsv(spanish_csv, "spanish")
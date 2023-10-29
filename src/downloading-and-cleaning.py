# Libraries
import pandas as pd

def importarCsv(path):
    return pd.read_csv(path)

df = importarCsv("../data/libros_mas_vendidos.csv")

def cleanCsv():
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
    
    books_csv.to_csv("../data/csv_projectII.csv", index=False)

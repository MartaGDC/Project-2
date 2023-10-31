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
    books_csv.sort_values(by = "order", inplace=True)
    books_csv.rename({"Título":"title"}, axis = 1, inplace = True)
    books_csv.rename({"Autor":"author"}, axis = 1, inplace = True)
    books_csv.rename({"Materias":"genre"}, axis = 1, inplace = True)
    books_csv.rename({"Editorial":"editorial"}, axis = 1, inplace = True)
    books_csv.rename({"País de publicación ":"country"}, axis = 1, inplace = True)
    books_csv.rename({"Idioma de publicación ":"language"}, axis = 1, inplace = True)
    books_csv.rename({"Idioma original ":"orig_language"}, axis = 1, inplace = True)
    books_csv.rename({"Nº páginas":"pages"}, axis = 1, inplace = True)
    books_csv.rename({"Fecha publicación ":"date"}, axis = 1, inplace = True)
    lst_fiction = ["Ficción moderna y contemporanea", "Obra de misterio y suspense", "Género policíaco y misterio",
                   "Novelas gráficas: manga", "Ficción histórica", "Narrativa romántica adulta y contemporánea",
                   "Narrativa romántica histórica", "Relatos sobre la familia y el hogar (infantil/juvenil)",
                    "Fantasía y realismo mágico (infantil/juvenil)", "Aventura histórica",
                    "Ficción de crimen y misterio (infantil/juvenil)", "Relatos de aventuras (infantil/juvenil)",
                    "FICCIÓN E HISTORIAS REALES INFANTILES Y JUVENILES", "Ficción general (infantil/juvenil)",
                    "Poesía de poetas individuales", "Relatos románticos y de relaciones interpersonales (infantil/juvenil)",
                    "Ficción clásica (infantil/juvenil)", "MITOS Y LEYENDAS NARRADOS COMO FICCIÓN", "Thriller (infantil/juvenil)",
                    "Cómics y novelas gráficas", "Libros de cuentos ilustrados"]
    lst_nofiction = ["Cuestiones personales y sociales: autoconocimiento y autoestima (infantil/juvenil)", "Ensayos literarios",
                     "Filosofía social y política", "Biografía: literaria", "Autoayuda y desarrollo personal",
                    "ESTILO DE VIDA, DEPORTE Y OCIO", "Mente, cuerpo y espíritu: pensamiento y práctica",
                    "Feminismo y teoría feminista", "Juegos de PC/ordenador/en línea: guías de estrategia", 
                    "Terapias complementarias, curación y salud", "Memorias", "Historia general y mundial", 
                    "TRATAMIENTOS Y MATERIAS ARTÍSTICAS", "Misterios, lo sobrenatural, monstruos y seres mitológicos (infantil/juvenil)",
                    "Familia y Salud", "Filosofía", "Antropología", "Forma física y alimentación", "Historias reales"]
    def clasif(x):
        if x["genre"] in lst_fiction:
            return "fiction"
        elif x["genre"] in lst_nofiction:
            return "non-fiction"
        else:
            return None
    books_csv["genres_clasif"] = books_csv.apply(clasif, axis=1)
    return books_csv

def saveCsv(df, name):
    df.to_csv(f"data/{name}_projectII.csv", index=False)
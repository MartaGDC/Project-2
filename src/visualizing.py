# Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


# AMAZON
def amazonGenres(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    amazon_genres = df["genre"].value_counts().plot.pie(autopct="%.1f%%");
    amazon_genres.set(title = "Percentage of fictional bestselling books in Amazon");
    amazon_genres.figure.savefig("figures/amazon_genres", dpi=1000);
    # Open images:
    os.system("start figures/amazon_genres.png")

def amazonGenresYear(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (2, 4)}, font_scale=0.5)
    sns.set_style("white")
    plt.figure()
    amazon_genres_years = sns.histplot(df, x="year_bought", hue = "genre", multiple="stack", bins = 3)
    amazon_genres_years.set(title = "Bestsellers in Amazon by genre and year")
    amazon_genres_years.figure.savefig("figures/amazon_genres_years", dpi=1000);
    # Open images:
    os.system("start figures/amazon_genres_years.png")
    
def amazonPrices(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 2)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    amazon_prices_box = sns.boxplot(x=df["price"])
    amazon_prices_box.set(title = "Distribution of prices in Amazon");
    amazon_prices_box.figure.savefig("figures/Distribution_of_prices_in_Amazon", dpi=1000);
    # Open images:
    os.system("start figures/Distribution_of_prices_in_Amazon.png")

def amazonPricesYear(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 5)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    fig, axs = plt.subplots(nrows=3)
    fig.suptitle("Distribution of prices by year")
    fig_2020 = df[df["year_bought"] == 2020].boxplot(column="price", ax=axs[0], vert=False)
    fig_2020.set_xlim(0,35)
    fig_2021 = df[df["year_bought"] == 2021].boxplot(column="price", ax=axs[1], vert=False)
    fig_2021.set_xlim(0,35)
    fig_2022 = df[df["year_bought"] == 2022].boxplot(column="price", ax=axs[2], vert=False)
    fig_2022.set_xlim(0,35)
    axs[0].set_title("2020")
    axs[1].set_title("2021")
    axs[2].set_title("2022")
    fig.savefig("figures/Distribution_of_prices_by_year_in_Amazon.png")
    # Open images:
    os.system("start figures/Distribution_of_prices_by_year_in_Amazon.png")
    
def amazonTopGenresYear(path):
    df = pd.read_csv(path)
    amazon_top_2020 = df[df["year_bought"] == 2020].head(10)
    amazon_top_2021 = df[df["year_bought"] == 2021].head(10)
    amazon_top_2022 = df[df["year_bought"] == 2022].head(10)
    amazon_top = pd.concat([amazon_top_2020, amazon_top_2021, amazon_top_2022])
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    amazon_genres_years = sns.countplot(data = amazon_top , hue ="genre", x="year_bought" )
    amazon_genres_years.set(title = "Genres of the top ten bestsellers by year in Amazon");
    amazon_genres_years.figure.savefig("figures/Genres_top_ten_by_year_Amazon", dpi=1000);
    # Open images:
    os.system("start figures/Genres_top_ten_by_year_Amazon.png")

# Indie bookshops 2020
def dbBookshopGenres(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    csv_genres = df["genres_clasif"].value_counts().plot.pie(autopct="%.1f%%");
    csv_genres.set(title = "Percentage of fictional bestselling books in Spain, 2020");
    csv_genres.figure.savefig("figures/Percentage_fictional_Spain_2020", dpi=1000);
    # Open images:
    os.system("start figures/Percentage_fictional_Spain_2020.png")
    
def dbBookshopTopGenres(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    sns.set(rc={"figure.figsize": (3, 4)}, font_scale=0.75)
    csv_top_genres = sns.countplot(data = df.head(10) , x ="genres_clasif")
    csv_top_genres.set(title = "Genres of the top ten bestsellers in Spain, 2020");
    csv_top_genres.figure.savefig("figures/Genres_top_ten_Spain_2020", dpi=1000);
   # Open images:
    os.system("start figures/Genres_top_ten_Spain_2020.png")
    
def dbBookshopEditorials(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (3, 6)}, font_scale=0.5)
    sns.set_style("white")
    plt.figure()
    csv_editorials = sns.countplot(data = df , x="editorial", order = df["editorial"].value_counts().iloc[:10].index)
    csv_editorials.set_xticklabels(csv_editorials.get_xticklabels(), rotation=35, horizontalalignment='right');
    csv_editorials.set(title = "Top 10 most selling editorials in Spain, 2020");
    csv_editorials.figure.savefig("figures/Top_10_editorials_Spain_2020", dpi=1000);
   # Open images:
    os.system("start figures/Top_10_editorials_Spain_2020.png")
    
def dbBookshopForeign(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (7, 6)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    csv_foreign = sns.countplot(data = df , x="orig_language")
    csv_foreign.set_xticklabels(csv_foreign.get_xticklabels(), rotation=10, horizontalalignment='right');
    csv_foreign.set(title = "Originary countries of bestselling books in Spain 2020");
    csv_foreign.figure.savefig("figures/Countries_bestselling_Spain_2020", dpi=1000);
   # Open images:
    os.system("start figures/Countries_bestselling_Spain_2020.png")
    

# Indie bookshops 2023 (web scrapping)
def webBookshopGenres(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    web_genres = df["genres_clasif"].value_counts().plot.pie(autopct="%.1f%%");
    web_genres.set(title = "Percentage of fictional bestselling books in Spain, 2023");
    web_genres.figure.savefig("figures/Percentage_fictional_Spain_2023", dpi=1000);
   # Open images:
    os.system("start figures/Percentage_fictional_Spain_2023.png")
    
def webPrices(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 2)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    web_prices_box = sns.boxplot(x=df["price"])
    web_prices_box.set(title = "Distribution of prices in Spain, 2023")
    web_prices_box.set_xlim(0,35);
    web_prices_box.figure.savefig("figures/Distribution_of_prices_in_Spain", dpi=1000);
    # Open images:
    os.system("start figures/Distribution_of_prices_in_Spain.png")

def webBookshopTopGenres(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    sns.set(rc={"figure.figsize": (3, 4)}, font_scale=0.75)
    web_top_genres = sns.countplot(data = df.head(10) , x ="genres_clasif")
    web_top_genres.set(title = "Genres of the top ten bestsellers by year in Spain, 2023");
    web_top_genres.figure.savefig("figures/Genres_top_ten_Spain_2023", dpi=1000);
    # Open images:
    os.system("start figures/Genres_top_ten_Spain_2023.png")

def webBookshopEditorials(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (3, 6)}, font_scale=0.5)
    sns.set_style("white")
    plt.figure()
    web_editorials = sns.countplot(data = df, x="editorial", order = df["editorial"].value_counts().iloc[:10].index)
    web_editorials.set_xticklabels(web_editorials.get_xticklabels(), rotation=35, horizontalalignment='right');
    web_editorials.set(title = "Top 10 most selling editorials in Spain, 2023");
    web_editorials.figure.savefig("figures/Top_10_editorials_Spain_2023", dpi=1000);
    # Open images:
    os.system("start figures/Top_10_editorials_Spain_2023.png")

def webBookshopForeign(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (7, 6)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    web_foreign = sns.countplot(data = df , x="orig_language")
    web_foreign.set_xticklabels(web_foreign.get_xticklabels(), rotation=10, horizontalalignment='right');
    web_foreign.set(title = "Originary countries of bestselling books in Spain 2023");
    web_foreign.figure.savefig("figures/Countries_bestselling_Spain_2023", dpi=1000);
    # Open images:
    os.system("start figures/Countries_bestselling_Spain_2023.png")


# Indie bookshops 2020, 2023
def bookshops(path_csv, path_web):
    csv = pd.read_csv(path_csv)
    web = pd.read_csv(path_web)
    shops = pd.concat([csv, web])
    def anyo(x):
        if x["price"] > 0:
            return "2023"
        else:
            return "2020"
    shops["year_best"] = shops.apply(anyo, axis=1)
    shops["orig_language"] = shops["orig_language"].apply(lambda x : "Castellano" if x == "Español" else x)
    shops.to_csv("data/shops_projectII.csv", index=False) 

def shopGenres(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    shop_genres = df["genres_clasif"].value_counts().plot.pie(autopct="%.1f%%");
    shop_genres.set(title = "Percentage of fictional bestselling books in Spain");
    shop_genres.figure.savefig("figures/Percentage_fictional_Spain", dpi=1000);
    # Open images:
    os.system("start figures/Percentage_fictional_Spain.png")

def shopGenresYear(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (3, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    shops_genres_years = sns.histplot(df, x="year_best", hue = "genres_clasif", multiple="stack", bins = 2)
    shops_genres_years.legend(["Fiction", "Non Fiction"], bbox_to_anchor=(1, 1));
    shops_genres_years.set(title = "Number of fictional bestselling books in spanish indie shops by year")
    shops_genres_years.figure.savefig("figures/Fictional_Spain_year", dpi=1000);
    # Open images:
    os.system("start figures//Fictional_Spain_year.png")
    
def shopTopGenresYear(path):
    df = pd.read_csv(path)
    shops_top_2020 = df[df["year_best"] == "2020"].head(10)
    shops_top_2023 = df[df["year_best"] == "2023"].head(10)
    shops_top = pd.concat([shops_top_2020, shops_top_2023])
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    shops_genres_years = sns.countplot(data = shops_top , hue ="genres_clasif", x="year_best" )
    shops_genres_years.set(title = "Genres of the top ten bestsellers by year in spanish indie shops");
    shops_genres_years.figure.savefig("figures/Genres_top_ten_by_year_Spain", dpi=1000);
    # Open images:
    os.system("start figures/Genres_top_ten_by_year_Spain.png")
    
def shopForeign(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (7, 6)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    shops_foreign = sns.countplot(data = df , x="orig_language", hue="year_best")
    shops_foreign.set_xticklabels(shops_foreign.get_xticklabels(), rotation=10, horizontalalignment='right');
    shops_foreign.set(title = "Originary countries of bestselling books in Spain in 2020 and 2023");
    shops_foreign.figure.savefig("figures/Countries_bestselling_Spain", dpi=1000);
    # Open images:
    os.system("start figures/Countries_bestselling_Spain.png")
    
    
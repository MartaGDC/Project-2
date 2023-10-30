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
    amazon_genres.figure.savefig("../images/amazon_genres", dpi=1000);

def amazonGenresYear(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (2, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    amazon_genres_years = sns.histplot(df, x="year_bought", hue = "genre", multiple="stack", bins = 3)
    amazon_genres_years.set(title = "Number of fictional bestselling books in Amazon by year")
    amazon_genres_years.legend(["Fiction", "Non Fiction"], bbox_to_anchor=(1, 1));
    amazon_genres_years.figure.savefig("../images/amazon_genres_years", dpi=1000);

def amazonPrices(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 2)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    amazon_prices_box = sns.boxplot(x=df["price"])
    amazon_prices_box.set(title = "Distribution of prices in Amazon");
    amazon_prices_box.figure.savefig("../images/amazon_distribution_prices", dpi=1000);

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
    fig.savefig("../figures/Distribution of prices by year in Amazon.png")
    
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
    amazon_genres_years.figure.savefig("../figures/Distribution of prices by year in Amazon.png")


# Indie bookshops 2020


    
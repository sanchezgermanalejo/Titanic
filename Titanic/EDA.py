import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(df):
    """Muestra información general del dataset."""
    print("\n📊 Información General del Dataset:")
    print(df.info())

    print("\n📊 Primeras Filas del Dataset:")
    print(df.head())

    print("\n📊 Valores Nulos en el Dataset:")
    print(df.isnull().sum())

    print("\n📊 Estadísticas Descriptivas:")
    print(df.describe())

def plot_survival_distribution(df):
    """Grafica la distribución de sobrevivientes y fallecidos."""
    sns.countplot(data=df, x="Survived", palette="coolwarm")
    plt.title("Distribución de Supervivientes")
    plt.xlabel("0 = No sobrevivió, 1 = Sobrevivió")
    plt.ylabel("Cantidad")
    plt.show()

def plot_class_distribution(df):
    """Grafica la distribución de pasajeros por clase."""
    sns.countplot(data=df, x="Pclass", palette="muted")
    plt.title("Distribución de Pasajeros por Clase")
    plt.xlabel("Clase del Boleto")
    plt.ylabel("Cantidad")
    plt.show()

def plot_age_distribution(df):
    """Grafica la distribución de edades."""
    plt.figure(figsize=(10,6))
    sns.histplot(df["Age"].dropna(), bins=30, kde=True, color="blue")
    plt.title("Distribución de Edades de los Pasajeros")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.show()

def plot_gender_distribution(df):
    """Muestra la cantidad de hombres y mujeres a bordo."""
    sns.countplot(data=df, x="Sex", palette="pastel")
    plt.title("Distribución por Género")
    plt.xlabel("Género")
    plt.ylabel("Cantidad")
    plt.show()

def plot_correlation_heatmap(df):
    """Muestra un heatmap de correlaciones entre variables numéricas."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matriz de Correlación")
    plt.show()

if __name__ == "__main__":
    # Cargar el dataset
    df = pd.read_csv("titanic.csv")

    # Análisis Exploratorio
    explore_data(df)

    # Visualizaciones
    plot_survival_distribution(df)
    plot_class_distribution(df)
    plot_age_distribution(df)
    plot_gender_distribution(df)
    plot_correlation_heatmap(df)

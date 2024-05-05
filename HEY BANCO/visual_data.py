import matplotlib.pyplot as plt
import pandas as pd



# Graficar el conteo de sentimientos
def plot_sentiment_counts(sentiment_counts):
    """
    Grafica el conteo de cada tipo de sentimiento.

    Parameters:
    sentiment_counts (pd.Series): Una serie pandas que contiene el conteo de cada tipo de sentimiento.

    Returns:
    None (Muestra la gráfica directamente).
    """
    plt.figure(figsize=(8, 5))
    sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
    plt.title('Distribución de Sentimientos de Tweets con VADER')
    plt.xlabel('Sentimiento')
    plt.ylabel('Número de Tweets')
    plt.show()

def basic_extract_keywords(text):
    """
    Extrae palabras clave de un texto eliminando puntuación y seleccionando solo palabras alfabéticas.

    Parameters:
    text (str): Texto del cual se extraerán las palabras clave.

    Returns:
    list: Lista de palabras clave extraídas del texto.
    """
    words = text.lower().split()  # Dividir el texto en palabras
    words_filtered = [word for word in words if word.isalpha()]  # Mantener solo palabras alfabéticas
    return words_filtered
 

def plot_words_sentiment(df):
    """
    Visualiza las palabras más frecuentes para cada sentimiento en tweets.

    Parameters:
    df (pd.DataFrame): DataFrame que contiene columnas 'sentiment' y 'basic_keywords'.

    Returns:
    None (Muestra las gráficas directamente).
    """
    basic_keywords_by_sentiment = df.groupby('sentiment')['basic_keywords'].sum()

    # Contar frecuencias de palabras clave para cada sentimiento
    basic_keyword_counts = {sentiment: pd.Series(keywords).value_counts().head(20) for sentiment, keywords in basic_keywords_by_sentiment.items()}

    # Visualizar las palabras más frecuentes para cada sentimiento
    for sentiment, counts in basic_keyword_counts.items():
        plt.figure(figsize=(10, 5))
        counts.plot(kind='bar', title=f'Top 20 palabras más frecuentes en tweets {sentiment}')
        plt.ylabel('Frecuencia')
        plt.xlabel('Palabras')
        plt.xticks(rotation=45)
        plt.show()






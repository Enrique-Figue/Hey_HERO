import pandas as pd
from preprocess import preprocess_text
from analyze_sentiment import get_vader_sentiment
from visual_data import plot_sentiment_counts, basic_extract_keywords, plot_words_sentiment

# Rutas de archivos
file_path = 'DB/heyDB.csv'  
output_file_path = 'DB/processed_data.csv'

def main():
    """
    Función principal que procesa un archivo CSV de tweets, realiza análisis de sentimiento y genera visualizaciones.
    """
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(file_path)

    # Aplicar preprocesamiento de texto a cada tweet en una nueva columna
    df['processed_tweet'] = df['tweet'].apply(preprocess_text)

    # Aplicar análisis de sentimiento utilizando VADER a cada tweet procesado
    df['sentiment'] = df['processed_tweet'].apply(get_vader_sentiment)

    # Extraer palabras clave básicas de cada tweet procesado
    df['basic_keywords'] = df['processed_tweet'].apply(basic_extract_keywords)

    # Guardar el DataFrame modificado en un nuevo archivo CSV
    df.to_csv(output_file_path, index=True)

    # Contar la cantidad de cada tipo de sentimiento
    sentiment_counts = df['sentiment'].value_counts()

    # Imprimir las cuentas de cada tipo de sentimiento
    print(sentiment_counts)

    # Crear y mostrar gráfico de conteo de sentimientos
    plot_sentiment_counts(sentiment_counts)

    # Crear y mostrar visualización de palabras y su sentimiento
    plot_words_sentiment(df)

    # Imprimir comentarios con sentimiento negativo
#    negative_comments = df[df['sentiment'] == 'Negativo']['tweet'].tolist()
#    print("Comentarios con Sentimiento Negativo:")
#    for comment in negative_comments:
#        print("- ", comment)

if __name__ == "__main__":
    main()


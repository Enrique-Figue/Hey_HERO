from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon') 

def get_vader_sentiment(text):
    """
    Clasifica un texto en Positivo, Neutral o Negativo utilizando el analizador de sentimientos VADER.

    VADER (Valence Aware Dictionary and sEntiment Reasoner) es una herramienta de análisis de sentimientos
    incluida en NLTK que asigna puntuaciones de polaridad (positivo, neutral o negativo) a un texto.

    Parameters:
    text (str): Texto que se va a analizar para determinar su sentimiento.

    Returns:
    str: Categoría de sentimiento ('Positivo', 'Neutral' o 'Negativo').
    """
    # Inicializar el analizador de sentimientos VADER
    sid = SentimentIntensityAnalyzer()
    
    # Obtener los puntajes de polaridad del texto
    score = sid.polarity_scores(text)
    
    # Determinar la categoría de sentimiento en base al puntaje compuesto
    if score['compound'] >= 0.05:
        return 'Positivo'
    elif score['compound'] > -0.05 and score['compound'] < 0.05:
        return 'Neutral'
    else:
        return 'Negativo'


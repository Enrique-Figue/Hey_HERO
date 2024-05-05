import re
import unicodedata
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

import nltk
nltk.download('stopwords')
nltk.download('punkt')

def remove_accents(text):
    """
    Elimina los acentos y caracteres diacríticos de un texto utilizando Unicode normalization.

    Parameters:
    text (str): Texto del cual se eliminarán los acentos.

    Returns:
    str: Texto sin acentos ni caracteres diacríticos.
    """
    normalized_text = unicodedata.normalize('NFKD', text)  # Normalizar el texto con Unicode
    ascii_text = normalized_text.encode('ascii', 'ignore').decode('utf-8', 'ignore')  # Convertir caracteres a ASCII eliminando acentos
    return ascii_text


def preprocess_text(text):
    """
    Realiza el preprocesamiento básico de un texto para su análisis de sentimientos.

    El preprocesamiento incluye:
    - Convertir el texto a minúsculas.
    - Eliminar acentos y caracteres especiales.
    - Tokenizar el texto en palabras.
    - Eliminar palabras de parada (stopwords) del idioma español.
    - Aplicar stemming (reducción a la forma base) a las palabras.

    Parameters:
    text (str): Texto que se va a preprocesar.

    Returns:
    str: Texto preprocesado y listo para análisis de sentimientos.
    """
    # Convertir texto a minúsculas y eliminar acentos
    text = remove_accents(text.lower())
    
    # Eliminar caracteres especiales y números usando expresiones regulares
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenización
    tokens = word_tokenize(text)
    
    # Eliminar stopwords del idioma español
    stop_words = set(stopwords.words('spanish'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming (reducción a la forma base de las palabras) usando SnowballStemmer
    stemmer = SnowballStemmer('spanish')
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    # Unir tokens procesados en una cadena de texto
    processed_text = ' '.join(stemmed_tokens)
    return processed_text
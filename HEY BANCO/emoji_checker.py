import pandas as pd
import regex as re
from collections import Counter

def count_emojis(text):
    # Use regex to find all emoji characters based on Unicode properties
    emoji_pattern = re.compile(r"\p{Emoji}")
    emojis = emoji_pattern.findall(text)
    
    # Filter out any characters that are digits ('0'-'9')
    emojis = [emoji for emoji in emojis if not emoji.isdigit()]
    
    emoji_counter = Counter(emojis)
    return emoji_counter

# Ruta al archivo Excel
file_path = "DB/heyDB.csv"

# Leer el archivo Excel en un dataframe de pandas
df = pd.read_csv(file_path)

# Nombre de la columna donde deseas contar emojis (por ejemplo, "tweet")
columna_deseada = "tweet"

# Contador total de emojis encontrados en la columna deseada
emojis_contados_total = Counter()

# Iterar sobre cada fila de la columna deseada y contar emojis
for fila in df.index:
    texto_celda = str(df.loc[fila, columna_deseada])  # Convertir a string para asegurar que se pueda buscar emojis
    emojis_contados_celda = count_emojis(texto_celda)
    emojis_contados_total += emojis_contados_celda

# Ordenar los emojis de mayor a menor según su conteo
emojis_ordenados = emojis_contados_total.most_common()

# Imprimir el recuento total de emojis encontrados en la columna deseada (ordenados de mayor a menor)
for emoji, count in emojis_ordenados:
    print(f"{emoji}: {count}")

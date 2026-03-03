import pandas as pd

# Carregar o dataset sem cabeçalho para verificar
df = pd.read_csv('/home/ubuntu/upload/crop_yield.csv', header=None)
print("Primeiras linhas:")
print(df.head())

# Tentar identificar colunas (baseado no conteúdo comum de crop yield)
# Provavelmente: Crop, Yield, Temperature, Humidity, Rainfall, Fertilizer/Pesticide?
# Vamos ver as estatísticas descritivas
print("\nInformações do DataFrame:")
print(df.info())

print("\nEstatísticas Descritivas:")
print(df.describe())

# Verificar valores únicos na primeira coluna (Cultura)
print("\nCulturas únicas:")
print(df[0].unique())

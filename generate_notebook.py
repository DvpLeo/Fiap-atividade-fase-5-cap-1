import nbformat as nbf
import pandas as pd

nb = nbf.v4.new_notebook()

# --- Célula de Título ---
nb.cells.append(nbf.v4.new_markdown_cell("# Análise de Produtividade Agrícola (Crop Yield)\nEste notebook contém a Análise Exploratória de Dados (EDA), Clusterização e Modelagem Preditiva para o dataset `crop_yield.csv`."))

# --- Importações ---
nb.cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Configurações de visualização
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)"""))

# --- Carregamento e Limpeza ---
nb.cells.append(nbf.v4.new_markdown_cell("## 1. Carregamento e Preparação dos Dados"))
nb.cells.append(nbf.v4.new_code_cell("""# Carregar dados
df = pd.read_csv('/home/ubuntu/upload/crop_yield.csv')

# Verificar tipos de dados e nulos
print(df.info())
print(df.head())

# Converter colunas numéricas (caso necessário)
# O dataset tem: Crop, Precipitation, Relative Humidity, Specific Humidity, Temperature, Yield
cols_numericas = df.columns[1:]
for col in cols_numericas:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remover nulos resultantes da conversão
df = df.dropna()
"""))

# --- EDA ---
nb.cells.append(nbf.v4.new_markdown_cell("## 2. Análise Exploratória de Dados (EDA)\nVamos entender a distribuição das variáveis e a relação com a produtividade (Yield)."))
nb.cells.append(nbf.v4.new_code_cell("""# Estatísticas descritivas
print("Estatísticas Descritivas:")
display(df.describe())

# Distribuição do Yield por Cultura
plt.figure(figsize=(12, 6))
sns.boxplot(x='Crop', y='Yield', data=df)
plt.title('Distribuição de Produtividade por Cultura')
plt.xticks(rotation=45)
plt.show()

# Matriz de Correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação')
plt.show()"""))

# --- Clusterização ---
nb.cells.append(nbf.v4.new_markdown_cell("## 3. Clusterização (Aprendizado Não Supervisionado)\nIdentificar padrões de produtividade e possíveis outliers."))
nb.cells.append(nbf.v4.new_code_cell("""# Preparar dados para clusterização (apenas numéricos)
X_cluster = df.drop('Crop', axis=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

# Aplicar KMeans
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualizar Clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperature at 2 Meters (C)', y='Yield', hue='Cluster', data=df, palette='viridis')
plt.title('Clusters de Produtividade vs Temperatura')
plt.show()

print("Contagem por Cluster:")
print(df['Cluster'].value_counts())"""))

# --- Modelagem Preditiva ---
nb.cells.append(nbf.v4.new_markdown_cell("## 4. Modelagem Preditiva (Regressão)\nCriação e comparação de 5 modelos de regressão."))
nb.cells.append(nbf.v4.new_code_cell("""# Codificar variável categórica 'Crop'
le = LabelEncoder()
df['Crop_Encoded'] = le.fit_transform(df['Crop'])

# Definir X e y
# Remover 'Yield' (alvo), 'Crop' (categórica original) e 'Cluster' (criada na etapa anterior)
X = df.drop(['Yield', 'Crop', 'Cluster'], axis=1)
y = df['Yield']

# Divisão Treino/Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronização
scaler_model = StandardScaler()
X_train_scaled = scaler_model.fit_transform(X_train)
X_test_scaled = scaler_model.transform(X_test)

# Definir Modelos
models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(),
    "Lasso": Lasso(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    results.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    })

results_df = pd.DataFrame(results).sort_values(by='R2', ascending=False)
print("Comparação de Modelos:")
display(results_df)"""))

# --- Conclusão ---
nb.cells.append(nbf.v4.new_markdown_cell("## 5. Discussão de Resultados\n### Pontos Fortes e Limitações\n- **Modelos Lineares:** Simples e interpretáveis, mas podem não capturar relações não-lineares complexas.\n- **Ensemble (RF/GB):** Geralmente mais precisos, mas podem sofrer overfitting se o dataset for muito pequeno.\n- **Limitações:** O dataset possui poucos registros (aprox. 150), o que pode afetar a generalização dos modelos."))

# Salvar o notebook
with open('/home/ubuntu/analise_produtividade.ipynb', 'w') as f:
    nbf.write(nb, f)

print("Notebook gerado com sucesso!")

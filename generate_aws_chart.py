import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Dados de custo
data = {
    'Região': ['N. Virginia (EUA)', 'São Paulo (Brasil)'],
    'EC2 (t3.micro)': [7.59, 10.66],
    'EBS (50GB gp3)': [4.00, 5.70]
}

df = pd.DataFrame(data)
df['Total Mensal'] = df['EC2 (t3.micro)'] + df['EBS (50GB gp3)']

# Configuração do gráfico
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Plotar barras empilhadas
p1 = plt.bar(df['Região'], df['EC2 (t3.micro)'], label='EC2 (t3.micro)', color='#FF9900')
p2 = plt.bar(df['Região'], df['EBS (50GB gp3)'], bottom=df['EC2 (t3.micro)'], label='EBS (50GB gp3)', color='#232F3E')

# Adicionar rótulos de valor
for i, total in enumerate(df['Total Mensal']):
    plt.text(i, total + 0.2, f'USD {total:.2f}', ha='center', fontweight='bold')

plt.ylabel('Custo Mensal (USD)')
plt.title('Comparação de Custos AWS: N. Virginia vs São Paulo')
plt.legend()
plt.ylim(0, 20)

# Salvar gráfico
plt.savefig('/home/ubuntu/aws_cost_comparison.png', dpi=300, bbox_inches='tight')
print("Gráfico de custos gerado com sucesso!")

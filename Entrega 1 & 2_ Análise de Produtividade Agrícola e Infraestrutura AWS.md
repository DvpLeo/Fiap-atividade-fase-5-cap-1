# Entrega 1 & 2: Análise de Produtividade Agrícola e Infraestrutura AWS

Este repositório contém as entregas para o projeto de análise de produtividade agrícola, incluindo a Análise Exploratória de Dados (EDA), clusterização e modelagem preditiva, bem como uma análise de infraestrutura em nuvem na AWS.

## Entrega 1: Análise de Produtividade Agrícola

O arquivo `analise_produtividade.ipynb` é um notebook Jupyter que detalha a análise do dataset `crop_yield.csv`. Ele aborda os seguintes pontos:

### 1. Análise Exploratória de Dados (EDA)

Nesta seção, a estrutura dos dados é compreendida, estatísticas descritivas são verificadas e padrões iniciais são identificados. Isso inclui a visualização da distribuição da produtividade por cultura e uma matriz de correlação entre as variáveis numéricas.

### 2. Clusterização (Aprendizado Não Supervisionado)

Utilizando o algoritmo K-Means, foram identificadas tendências de produtividade e possíveis outliers no dataset. Os dados foram padronizados antes da aplicação do algoritmo para garantir que todas as variáveis contribuíssem igualmente para a formação dos clusters.

### 3. Modelagem Preditiva (Regressão Supervisionada)

Foram criados e comparados 5 modelos diferentes de regressão para prever a produtividade (`Yield`). As boas práticas de Machine Learning foram seguidas, incluindo a separação dos dados em conjuntos de treino e teste, padronização das features e avaliação com métricas adequadas (MAE, MSE, RMSE, R²). Os modelos utilizados foram:

*   Regressão Linear
*   Ridge Regression
*   Lasso Regression
*   Random Forest Regressor
*   Gradient Boosting Regressor

### 4. Discussão de Resultados

Os pontos fortes e limitações de cada modelo são discutidos, considerando a complexidade e o tamanho do dataset. Modelos de ensemble (Random Forest, Gradient Boosting) geralmente apresentaram melhor desempenho, mas a limitação do volume de dados (aproximadamente 150 registros) é um fator importante a ser considerado na generalização dos resultados.

## Entrega 2: Infraestrutura em Nuvem (AWS)

Esta seção apresenta uma análise de custos e uma escolha estratégica de região na AWS para hospedar a aplicação, considerando os requisitos de configuração e restrições legais.

### 1. Estimativa de Custos (AWS Calculator – 100% On-Demand)

A estimativa de custos foi realizada para uma configuração de máquina com 2 CPUs, 1 GiB de memória, até 5 Gbps de rede e 50 GB de armazenamento (HD), utilizando o sistema operacional Linux. Os custos foram comparados entre as regiões de São Paulo (Brasil) e Virgínia do Norte (EUA).

**Configuração Detalhada:**
*   **Instância EC2:** t3.micro (2 vCPU, 1 GiB RAM, até 5 Gbps de rede)
*   **Armazenamento EBS:** 50 GB (gp3)
*   **Modelo de Preço:** On-Demand
*   **Sistema Operacional:** Linux

**Comparativo de Custos Mensais (Valores Aproximados em USD):**

| Componente          | N. Virginia (EUA) | São Paulo (Brasil) |
| :------------------ | :---------------- | :----------------- |
| EC2 (t3.micro)      | $7.59             | $10.66             |
| EBS (50GB gp3)      | $4.00             | $5.70              |
| **Total Mensal**    | **$11.59**        | **$16.36**         |

**Gráfico Comparativo de Custos:**

![Comparativo de Custos AWS](https://private-us-east-1.manuscdn.com/sessionFile/wx6A0963zI5OXrCNwddQgA/sandbox/kMuTN0eNf6YplCSTHbBIDj-images_1771870235967_na1fn_L2hvbWUvdWJ1bnR1L2F3c19jb3N0X2NvbXBhcmlzb24.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvd3g2QTA5NjN6STVPWHJDTndkZFFnQS9zYW5kYm94L2tNdVROMGVOZjZZcGxDU1RIYkJJRGotaW1hZ2VzXzE3NzE4NzAyMzU5NjdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyRjNjMTlqYjNOMFgyTnZiWEJoY21semIyNC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Aa9-GJtxyM7jfnhJNN5AA4RPu3cpkPmPgJeTfCJgE7Ymzz556Mfm~QVP1c3QVanSVEjqI2zWQ7kIaKHZcC5h4LlAXyAw0azuPr-7XO0afnB0qH4bWYPt1WFZQfAohcHO6BEFj2-Y7lMO7EgB5nW-ors5h25RI0Miw~trIZSrC6pzlkD1JIgQBtTIX-9w9Q5S4Ru83arvHrksB8c1DWTqHG2Y6tH~JezpG8~FGuCiv5c76aqNbZ7X0QoW2e9n7Z9vGOLjDKt4vx8ZviomF5qtiDMs71F0UxHn~C0oQW6i~Z43KDc0r2yO0u29mpfjYJ0Hl~NLe~~OzqZTfbXnJWDEhg__)

**Simulação de Prints da Calculadora AWS:**

Para a região de **Virgínia do Norte (us-east-1)**, ao configurar uma instância `t3.micro` (Linux) e 50 GB de armazenamento EBS `gp3` no AWS Pricing Calculator, o custo mensal estimado para a instância EC2 seria de aproximadamente $7.59 e para o EBS de $4.00, totalizando cerca de $11.59. A interface da calculadora exibiria esses valores discriminados por serviço e um total mensal.

Para a região de **São Paulo (sa-east-1)**, com a mesma configuração (`t3.micro` Linux e 50 GB EBS `gp3`), o custo mensal estimado para a instância EC2 seria de aproximadamente $10.66 e para o EBS de $5.70, resultando em um total de cerca de $16.36. A calculadora AWS refletiria esses valores mais elevados, destacando a diferença de preço entre as regiões.

### 2. Escolha Estratégica

Considerando os requisitos de acesso rápido aos dados dos sensores e as restrições legais para armazenamento no exterior, a região a ser escolhida é **São Paulo (sa-east-1)**.

**Justificativa Técnica:**

*   **Latência:** Para aplicações que dependem de acesso rápido a dados de sensores localizados no Brasil, a latência é um fator crítico. Hospedar a infraestrutura na região de São Paulo minimiza a distância física entre os usuários/sensores e os servidores, resultando em menor latência e melhor experiência do usuário. A latência para usuários no Brasil seria significativamente maior se a infraestrutura estivesse em Virgínia do Norte.
*   **Legislação:** Restrições legais para armazenamento de dados no exterior são comuns em muitos países, especialmente para dados sensíveis ou regulamentados. Manter os dados dentro do território brasileiro (São Paulo) garante a conformidade com as leis locais de proteção de dados e privacidade, evitando possíveis complicações legais e multas.
*   **Custo vs. Benefício:** Embora a região de São Paulo seja mais cara em termos de custo direto de infraestrutura (aproximadamente 40% a mais que Virgínia do Norte para a configuração especificada), os benefícios de baixa latência e conformidade legal superam o custo adicional. A economia de custos em Virgínia do Norte não justificaria os riscos operacionais e legais associados.
*   **Transferência de Dados:** Embora a transferência de dados de saída seja mais cara em São Paulo, a proximidade com a origem dos dados (sensores no Brasil) pode reduzir a quantidade total de dados transferidos para fora da região, mitigando parte dessa diferença de custo.

Em resumo, a escolha da região de São Paulo, apesar do custo mais elevado, é a mais adequada para garantir a performance, a conformidade legal e a melhor experiência para os usuários locais da aplicação.


 🛡️ Projeto: O Dilema do Falso Positivo – Sistema de Prevenção a Fraudes

Este projeto simula um cenário real enfrentado diariamente por analistas de prevenção a fraudes: o dilema entre bloquear transações suspeitas (correndo o risco de frustrar clientes legítimos) ou deixar transações potencialmente fraudulentas passarem (assumindo risco financeiro).

Criado por Daniel Victor Simões Neves, este projeto faz parte de seu portfólio profissional como entusiasta em fraudes, machine learning e user experience. Ele foi desenvolvido para demonstrar competências essenciais exigidas por empresas que atuam com prevenção a fraudes em fintechs, bancos digitais e e-commerces.

---

🎯 Objetivos do Projeto

• Simular uma base de transações bancárias realistas
• Engenhar variáveis contextuais a partir das transações
• Desenvolver um sistema de alertas baseado em regras de negócio
• Avaliar a performance do sistema utilizando métricas clássicas de detecção de fraudes
• Visualizar os resultados e scores de risco comparados à fraude real

---

🧠 Problema: O Falso Positivo
Na detecção de fraudes, um dos principais desafios é o falso positivo:
Classificar como fraude uma transação que na verdade é legítima.

• 🔒 Bloquear um cliente legítimo = perda de confiança e churn
• 💸 Deixar passar uma fraude real = prejuízo financeiro

Este projeto aborda este dilema propondo uma análise contextual do comportamento do usuário, sem depender inicialmente de algoritmos de machine learning.

---

🧠 Conceitos Envolvidos

- Falso Positivo: quando uma transação legítima é classificada como fraude
- Features Contextuais: tempo, canal, dispositivo, localização, valor
- Sistema de Regras: lógica de negócio que simula alertas em tempo real
- Análise de Performance: recall, precisão, acurácia, matriz de confusão

---

🛠️ Metodologia

1. Simulação de Dados
   • Dataset com 10.000 transações
   • Variáveis: valor, data/hora, canal, localização, dispositivo, ID do usuário
   • 2% das transações marcadas como fraudulentas
   • Simulação inclui outliers de valor e horários suspeitos

---

2. Engenharia de Features (arquivo features.py)

• Criação de variáveis como:
o Hora da transação
o Transações por hora/dia por usuário
o Distância geográfica entre transações
o Troca de dispositivo/canal
• Essas features ajudam a entender comportamentos atípicos

---

3. Sistema de Regras (arquivo regras.py)

• Regras heurísticas desenvolvidas com base nas features criadas:
o Transação em horário incomum
o Valor muito acima da média
o Geolocalização incompatível com histórico
o Mudança abrupta de canal ou dispositivo
• Cada regra contribui com um score de risco
• Geração de alertas com base no score final

---

4. Análise de Performance

• Métricas utilizadas:
o Precisão (Precision)
o Revocação (Recall)
o Matriz de confusão
• Visualização da relação entre score de risco e transações fraudulentas reais

---

📊 Principais Resultados
• O sistema baseado em regras simples foi capaz de capturar boa parte das transações fraudulentas com alta taxa de recall.
• A análise visual mostrou que scores mais altos estão de fato associados às fraudes.
• Identificamos também falsos positivos, reforçando o desafio de calibrar regras para minimizar atrito com clientes.
• O sistema serviu como uma prova de conceito, mostrando que é possível gerar inteligência mesmo sem algoritmos complexos.

---

## 🗂️ Estrutura do Projeto

```
fraude-falso-positivo/
│
├── data/                  # Dataset simulado (transacoes.csv)
│
├── notebooks/             # Etapas do projeto
│   └── 01_EDA.ipynb            → Análise exploratória
│   └── 02_Regras.ipynb         → Aplicação das regras
│   └── 03_Visualizacoes.ipynb  → Avaliação visual dos resultados
│
├── src/
│   └── features.py        # Funções de engenharia de variáveis
│   └── regras.py          # Regras de negócio para scoring
│
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto

```

---

## 🚀 Como rodar o projeto

1. Clone este repositório:

```
git clone https://github.com/seu-usuario/fraude-falso-positivo.git
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute os notebooks na pasta `notebooks/` na ordem 01 → 03.

---

## 📊 Exemplos de Outputs

- Score de risco vs. fraude real
- Matriz de confusão da regra
- Análise de variáveis com mais impacto em alertas

---

🧪 Tecnologias Utilizadas
• Python (Pandas, NumPy, Matplotlib, Seaborn)
• Jupyter Notebooks
• Git & GitHub

---

---

👨‍💻 Sobre o Autor

Daniel Victor Simões Neves

Estudante de Ciência de Dados | Focado em Prevenção a Fraudes, AML, e Machine Learning
Com este projeto, Daniel mostra domínio prático em engenharia de dados, lógica de negócio antifraude e habilidades que se alinham diretamente às demandas de empresas que valorizam segurança, inteligência e experiência do cliente.
📧 LinkedIn - https://www.linkedin.com/in/daniel-victor-/
• GitHub: - https://github.com/DanielVictor-Dev

---


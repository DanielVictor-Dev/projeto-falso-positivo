
 🧠 Projeto: Sistema Analítico de Anomalias em Transações Bancárias
 
Este projeto simula o processo completo de desenvolvimento de um sistema de detecção de anomalias em transações financeiras, com foco em engenharia de variáveis, modelagem de regras heurísticas, visualização de métricas de performance e prototipagem de soluções baseadas em dados.

O objetivo é demonstrar competências fundamentais de um Cientista de Dados Júnior em ambientes de negócios reais — como bancos digitais, fintechs ou e-commerces — ao construir um sistema interpretável e de rápida iteração.

🎯 Objetivos Técnicos

- Simular uma base de dados realista com comportamento de usuários financeiros

- Aplicar técnicas de engenharia de features contextuais

- Implementar um sistema de pontuação baseado em regras de negócio

- Avaliar a performance das regras com métricas de classificação

- Visualizar padrões, alertas e trade-offs em um ambiente simulado

📚 Principais Habilidades Demonstradas
Simulação e análise de dados transacionais

Criação de features derivadas do contexto (tempo, localização, canal, etc.)

Desenvolvimento de sistemas de pontuação baseados em lógica de negócio

Avaliação de sistemas classificadores com métricas como precisão, revocação e matriz de confusão

Organização modular do código em Python

Visualização e interpretação dos resultados para tomada de decisão

🛠️ Metodologia

Simulação de Dados
Dataset com 10.000 transações fictícias

Variáveis: valor, data/hora, canal, localização, dispositivo, ID do usuário

Inserção controlada de padrões anômalos (~2% de fraudes)

Outliers simulados com horários incomuns, valores extremos e trocas bruscas de canal/dispositivo

Engenharia de Features (features.py)
Extração de variáveis contextuais como:

Hora da transação

Frequência de transações por hora/dia

Distância geográfica entre transações consecutivas

Mudanças súbitas de canal ou dispositivo

Features construídas com foco em comportamento do usuário ao longo do tempo

Sistema de Regras (regras.py)
Regras heurísticas baseadas nas features derivadas:

Transação em horário atípico

Valor acima da média histórica do usuário

Localização incompatível com transações anteriores

Mudança abrupta de dispositivo ou canal

Cada regra gera uma pontuação de risco agregada para posterior análise

Avaliação de Performance
Métricas utilizadas:

Precisão (Precision)

Revocação (Recall)

Matriz de confusão

Visualizações:

Score de risco vs. transações rotuladas

Distribuição de alertas por regras acionadas

Curva de trade-off entre recall e falsos positivos

📊 Principais Resultados

- O sistema foi capaz de identificar com eficácia comportamentos atípicos nas transações

- A análise visual mostrou forte correlação entre score de risco e transações anômalas

- Foram identificados falsos positivos, reforçando a importância de balanceamento entre precisão e cobertura

- O projeto demonstra como é possível gerar valor com modelos simples, interpretáveis e de rápida implementação

🗂️ Estrutura do Projeto
bash
Copiar
Editar
analise-transacoes/
│
├── data/                  # Dataset simulado (transacoes.csv)
│
├── notebooks/             # Jupyter Notebooks com as etapas do projeto
│   ├── 01_EDA.ipynb            → Análise exploratória dos dados
│   ├── 02_Regras.ipynb         → Aplicação das regras heurísticas
│   └── 03_Visualizacoes.ipynb  → Avaliação visual dos resultados
│
├── src/
│   ├── features.py         # Funções para engenharia de variáveis
│   └── regras.py           # Regras de negócio e pontuação de risco
│
├── requirements.txt        # Bibliotecas necessárias
└── README.md               # Documentação do projeto
🚀 Como Executar o Projeto
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/analise-transacoes.git
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute os notebooks em sequência na pasta notebooks/.

📎 Tecnologias Utilizadas
Python (Pandas, NumPy)

Visualização com Seaborn e Matplotlib

Jupyter Notebook

Git & GitHub

✅ Diferenciais do Projeto
Foco em pipeline completo de ciência de dados, desde simulação até visualização

Código modular e reutilizável em diferentes cenários de negócio

Interpretação clara dos resultados para comunicação com áreas não técnicas



---

---

👨‍💻 Sobre o Autor

Daniel Victor Simões Neves

Estudante de Ciência de Dados | Focado em Prevenção a Fraudes, AML, e Machine Learning
Com este projeto, Daniel mostra domínio prático em engenharia de dados, lógica de negócio antifraude e habilidades que se alinham diretamente às demandas de empresas que valorizam segurança, inteligência e experiência do cliente.
📧 LinkedIn - https://www.linkedin.com/in/daniel-victor-/
• GitHub: - https://github.com/DanielVictor-Dev

---


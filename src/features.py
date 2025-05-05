# Funções de engenharia de features para prevenção a fraudes


import pandas as pd

def adicionar_features(df):
    df = df.copy()

    df['turno'] = df['hora'].apply(lambda x: 'madrugada' if x < 6 else 
                                               'manha' if x < 12 else 
                                               'tarde' if x < 18 else 'noite')

    df['valor_alto'] = df['valor'] > 1000
    df['canal_suspeito'] = df['canal'].isin(['Web', 'POS'])

    local_por_usuario = df.groupby('id_usuario')['localizacao'].transform(lambda x: x.nunique())
    df['localizacao_rara'] = local_por_usuario > 2

    freq_usuario = df['id_usuario'].value_counts()
    df['frequencia_usuario'] = df['id_usuario'].map(freq_usuario)
    df['alta_frequencia'] = df['frequencia_usuario'] > freq_usuario.quantile(0.90)

    return df


# Sistema de alertas baseado em regras simples de negócio

def gerar_score_alerta(df):
    df = df.copy()
    df['score_alerta'] = 0

    df['score_alerta'] += df['valor_alto'] * 2
    df['score_alerta'] += df['canal_suspeito'] * 1
    df['score_alerta'] += df['localizacao_rara'] * 1
    df['score_alerta'] += df['alta_frequencia'] * 2
    df['score_alerta'] += df['turno'].isin(['madrugada', 'noite']) * 1

    df['alerta'] = df['score_alerta'] >= 4
    return df


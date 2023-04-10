rendimento_mensal= 0
contador = 0
maior_faturamento = float('-inf')
menor_faturamento = float('inf')
dias_faturamento_maior = []
def remover_faturamentos_zero(relatorio):
    faturamento_filtrado = []
    for faturamento in relatorio['faturamento']:
        if faturamento['valor'] != 0:
            faturamento_filtrado.append(faturamento)
    return {'mes': relatorio['mes'], 'faturamento': faturamento_filtrado}


relatorio_bruto = {
  "mes": "abril",
  "faturamento": [
    { "dia": 1, "valor": 1500 },
    { "dia": 2, "valor": 2500 },
    { "dia": 3, "valor": 3200 },
    { "dia": 4, "valor": 1200 },
    { "dia": 5, "valor": 1800 },
    { "dia": 6, "valor": 2100 },
    { "dia": 7, "valor": 3000 },
    { "dia": 8, "valor": 3500 },
    { "dia": 9, "valor": 2700 },
    { "dia": 10, "valor": 4000 },
    { "dia": 11, "valor": 2900 },
    { "dia": 12, "valor": 0 },
    { "dia": 13, "valor": 1800 },
    { "dia": 14, "valor": 2900 },
    { "dia": 15, "valor": 3200 },
    { "dia": 16, "valor": 2700 },
    { "dia": 17, "valor": 3800 },
    { "dia": 18, "valor": 4200 },
    { "dia": 19, "valor": 2800 },
    { "dia": 20, "valor": 3300 },
    { "dia": 21, "valor": 2900 },
    { "dia": 22, "valor": 3100 },
    { "dia": 23, "valor": 0 },
    { "dia": 24, "valor": 4100 },
    { "dia": 25, "valor": 3500 },
    { "dia": 26, "valor": 4200 },
    { "dia": 27, "valor": 2800 },
    { "dia": 28, "valor": 0 },
    { "dia": 29, "valor": 3300 },
    { "dia": 30, "valor": 3600 }
  ]
}

relatorio = remover_faturamentos_zero(relatorio_bruto)

for faturamentos in relatorio['faturamento']:
    # print(faturamentos['dia'], faturamentos['valor'])
    rendimento_mensal += faturamentos['valor']
    contador += 1

    if maior_faturamento < faturamentos['valor']:
        maior_faturamento = faturamentos['valor']
        dia_menor = faturamentos['dia']

    if menor_faturamento > faturamentos['valor']:
        menor_faturamento = faturamentos['valor']
        dia_maior = faturamentos['dia']
    
media = rendimento_mensal/contador

for faturamentos in relatorio['faturamento']:
    
    print(faturamentos['dia'], faturamentos['valor'])
    if media < faturamentos['valor']:
        dias_faturamento_maior.append(faturamentos['dia'])

print(f"O faturamento médio foi de {media}")
print(f"Os dias que o faturamento foi acima da media")
print(dias_faturamento_maior)
print(f"O dia {dia_menor} foi o com o menor faturamento de {menor_faturamento}")
print(f"O dia {dia_maior} foi o com o menor faturamento de {maior_faturamento}")
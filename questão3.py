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
 {
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
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

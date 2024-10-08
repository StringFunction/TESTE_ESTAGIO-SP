import json

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


# Abrir o arquivo JSON em modo de leitura
with open("dados.json", "r") as file:
    # Carregar o conteúdo do arquivo
    dados = json.load(file)

faturamento_diario = dados

# Extrair os valores de faturamento
valores = [item['valor'] for item in faturamento_diario if item['valor'] != 0.0]

# Cálculo do menor e maior faturamento
menor_faturamento = min(valores)
maior_faturamento = max(valores)

# Cálculo da média mensal
media_mensal = sum(valores) / len(valores)  # média considerando todos os dias

# Contagem de dias com faturamento acima da média
dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

# Exibir os resultados
print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
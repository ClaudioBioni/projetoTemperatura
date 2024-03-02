# Função para validar a temperatura dentro do intervalo permitido (-60 a +50 graus Celsius)
def validar_temperatura(temp):
    return -60 <= temp <= 50

# Função para converter o número do mês para o nome do mês
def converter_mes(num_mes):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return meses[num_mes - 1]

# Inicialização das variáveis
temperaturas_maximas = [] 
meses_escaldantes = 0
maior_temperatura = float("-inf")
menor_temperatura = float("inf")
mes_mais_escaldante = ""
mes_menos_quente = ""
temperatura_media = 0 

# Loop para coletar dados de temperatura de cada mês
for mes in range(1, 13):
    temperatura_valida = False
    while not temperatura_valida: 
        try:
            temp_max = float(input(f"Digite a temperatura máxima para o mês {converter_mes(mes)}: "))
            if not validar_temperatura(temp_max):
                print("Temperatura inválida. Por favor, digite uma temperatura entre -60 e 50 graus Celsius.")
                continue
            temperatura_valida = True
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    # Atualização das temperaturas máximas, temperatura média e contagem de meses escaldantes
    temperaturas_maximas.append(temp_max) 
    temperatura_media += temp_max 
    if temp_max > 33:
        meses_escaldantes += 1
    if temp_max > maior_temperatura:
        maior_temperatura = temp_max
        mes_mais_escaldante = converter_mes(mes)
    if temp_max < menor_temperatura:
        menor_temperatura = temp_max
        mes_menos_quente = converter_mes(mes)

# Cálculo da temperatura média anual
temperatura_media /= 12

# Exibição dos resultados
print("\nAnálise dos dados meteorológicos de 2021:")
print(f"Temperatura média máxima anual: {temperatura_media:.2f} graus Celsius")
print(f"Quantidade de meses escaldantes: {meses_escaldantes}")
print(f"Mês mais escaldante do ano: {mes_mais_escaldante}")
print(f"Mês menos quente do ano: {mes_menos_quente}")

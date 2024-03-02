# Validação se a temperatura inserida está dentro dos parametros permitidos
def validar_temperatura(temp):
    return -60 <= temp <= 50
    
# Converter o número do mês para o nome dele
def converter_mes(num_mes):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return meses[num_mes - 1]

# Inicialização das variáveis
temperaturas_maximas = [] 
meses_escaldantes = 0
maior_temperatura = float("-inf")
menor_temperatura = float("inf")
mes_escaldante = ""
mes_menos_quente = ""
temperatura_media = 0 

for mes in range(1, 13):
    temperatura_valida = False
    while not temperatura_valida: 
            temp_max = float(input(f"Insira a temperatura máxima para o mês {converter_mes(mes)}: "))
            if not validar_temperatura(temp_max):
                print("Temperatura inválida. Insira uma temperatura entre -60 e 50 graus Celsius.")
                continue
            temperatura_valida = True

    # Calculo das temperaturas máximas, média e meses escaldantes
    temperaturas_maximas.append(temp_max)
    temperatura_media += temp_max #Input das temperaturas
    if temp_max > 33:
        meses_escaldantes += 1
    if temp_max > maior_temperatura:
        maior_temperatura = temp_max
        mes_escaldante = converter_mes(mes)
    if temp_max < menor_temperatura:
        temp_max = menor_temperatura
        mes_menos_quente = converter_mes(mes)

temperatura_media /=12

# Resultados
print(f'Media de Temperatura anual: {temperatura_media:.1f}')
print(f'Quantidade de meses escaldantes: {meses_escaldantes}')
print(f'Mês mais escaldante: {mes_escaldante}')
print(f'Mês menos quente: {mes_menos_quente}')
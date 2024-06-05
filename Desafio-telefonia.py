# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
    limite_basico = 10
    limite_intermediário = 20

    if consumo <= limite_basico:
        return"Plano básico: Ideal para uso leve."
    
    elif consumo <= limite_intermediário:
       return "Plano Intermediário: Adequado para uso moderado."
    
    elif consumo <= limite_avancado:
        return "Plano Avançado: Recomendado para uso intenso."

    else:
        return "Plano personalizado: Entre em contato para obter opções personalizadas."


consumo = float(input("Insira o consumo médio mensal de dados (em GB): "))
print(recomendar_plano(consumo))




    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
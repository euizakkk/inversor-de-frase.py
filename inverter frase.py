def inverter_str(frase):
    """
    :frase:>>> recebe uma frase que será invertida
    A saida tem o nome de 'frase_invertida' 
    """
    global frase_invertida
    frase_invertida = []
    tamanho_para_inverter = 0
    tamanho_da_frase = len(frase)
    for l in frase:
        frase_invertida.insert(tamanho_para_inverter,l)
    for p in range(1,tamanho_da_frase+1):
        tamanho_para_inverter +=1
    return frase_invertida

inverter_str(str(input("Digite uma frase> ")))
print(frase_invertida)
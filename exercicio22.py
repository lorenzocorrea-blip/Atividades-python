

temperatura = float(input("Digite a temperatura do dia em °C: ")) # lê a temperatura do dia em °C
if temperatura < 0: # se a temperatura for menor que 0, ela é abaixo        de zero e há risco de geada
    print("Abaixo de zero — risco de geada!") 
elif temperatura < 10:
    print("Muito frio — capriche no agasalho!")
elif temperatura < 18:
    print("Frio!")
elif temperatura < 25:
    print("Agradável!")
else:
    print("Calor!")
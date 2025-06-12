vida_maxima = 0
vida_actual = 0

porcentaje_vida_restante = 0

print("bienvenido \n a continuacion calcularemos el porcentaje de vida restante de un personaje")

vida_maxima = int(input("porcentaje vida maxima: "))
vida_actual = int(input(" porcentaje vida actual: "))


porcentaje_vida_restante = (vida_actual/vida_maxima) * 100

print(f"tu porcentaje de vida actual es: {porcentaje_vida_restante}%")


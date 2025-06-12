total_misiones = 0
misiones_completadas = 0
porcentaje_misiones_completadas = 0

print("bienvenido \n a continuacion calcularemos el porcentaje de las misiones completadas")

total_misiones = int(input("total de las misiones a completar: "))
misiones_completadas = int(input("misiones completadas: "))


porcentaje_misiones_completadas = (misiones_completadas/total_misiones) * 100

print(f"tu porcentaje de vida actual de misiones completadas es: {porcentaje_misiones_completadas}%")


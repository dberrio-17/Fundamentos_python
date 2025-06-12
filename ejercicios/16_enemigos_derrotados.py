total_enemigos = 0
enemigos_derrotados = 0
porcentaje_enemigos_derrotados = 0

print("bienvenido \n a continuacion calcularemos el porcentaje de los enemigos derrotados")

total_enemigos = int(input("total de los enemigos: "))
enemigos_derrotados = int(input("enemigos derroatods: "))


porcentaje_misiones_completadas = (enemigos_derrotados/total_enemigos) * 100

print(f"tu porcentaje de enemigos derrotados es: {porcentaje_misiones_completadas}%")


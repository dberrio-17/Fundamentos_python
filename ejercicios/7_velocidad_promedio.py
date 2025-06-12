distancia_recorrida_vehiculo = 0
tiempo_tomado_vehiculo = 0
velocidad_promedio_vehiculo = 0

print("bienvenidos \n calcularemos la velocidad promedio vehiculo")

distancia_recorrida_vehiculo = int(input("distancia recorrida(km): "))
tiempo_tomado_vehiculo = int(input("tiempo tomado(horas): "))


velocidad_promedio_vehiculo = distancia_recorrida_vehiculo/tiempo_tomado_vehiculo

print(f"la velocidad promedio de tu vehiculo es: {velocidad_promedio_vehiculo} km/h")


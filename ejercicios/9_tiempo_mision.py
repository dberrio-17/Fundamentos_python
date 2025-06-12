tiempo_total_mision = 0
tiempo_transcurrido_mision = 0
timepo_completado = 0

print("bienvenido \n a continuacion calcularemos el tiempo restante para completar la mision")

tiempo_total_mision = int(input("tiempo total de la mision: "))
tiempo_transcurrido_mision = int(input("tiempo transcurrido de la mison: "))

timepo_completado = timepo_completado - tiempo_transcurrido_mision


print(f"tiempo restante para completar la mision es de: {timepo_completado}")


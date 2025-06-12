hora = 0
minutos = 0
segundos = 0
total_tiempo_jugado = 0


print("bienvenidos \ncalcularemos el tiempo total jugado")

hora = int(input("horas jugadas: "))
minutos = int(input("minutos jugados: "))
segundos = int(input("segundos jugados: ")) 

total_tiempo_jugado = (hora * 3600) + (minutos * 60) + segundos

print(f"tu tiempo total jugado es {total_tiempo_jugado}")

           
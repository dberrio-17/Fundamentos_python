daño_base_atque = 0
multiplicador_critico = 0

daño_final = 0


print("bienvenidos \n calcularemos el daño critico del ataque ")

daño_base_atque = int(input(" daño base del ataque: "))
multiplicador_critico = int(input("cual es el multiplicador del ataque: "))
experiencia_total_acumulada = daño_base_atque * multiplicador_critico

print(f"el daño critico del ataque es: {experiencia_total_acumulada}")

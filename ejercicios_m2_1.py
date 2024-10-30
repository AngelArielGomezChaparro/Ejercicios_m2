
#import es para importar una bibliote
#math es el nombre de aquella biblioteca

import math

# constantes
M = 47  # Masa del huevo en gramos (huevo pequeño)
p = 1.038  # Densidad en g/cm³
c = 3.7  # Capacidad calorífica específica en J/(g·K)
K = 5.4 * math.pow(10, -3)  # Conductividad térmica en W/(cm·K)
Tw = 100  # Temperatura de ebullición del agua en °C
Ty = 70  # Temperatura máxima de la yema en °C

To = float(input("Enter the original temperature of the egg (in °C): "))

# Usando la fórmula
dividiendo = math.pow(M, 2/3) * (c * math.pow(p, (1/3)))
divisor = (K * math.pow(math.pi, 2)) * math.pow((4 * math.pi) / 3, (2/3))
resultado = dividiendo / divisor

resultado2 = math.log((0.76 * To - Tw) / (Ty - Tw))

segundos = resultado * resultado2
minutos = round(segundos / 60)

# Mostrar el resultado
print(f"Time to reach the maximum temperature for a soft-boiled egg: {segundos:.2f} seconds ({minutos} minutes)")



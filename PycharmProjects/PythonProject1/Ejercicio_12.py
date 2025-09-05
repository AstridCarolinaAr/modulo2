import random

frecuencias_sumas = {}
for suma in range(2, 13):
    frecuencias_sumas[suma] = 0
for _ in range(10000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    frecuencias_sumas[suma] += 1
print("Frecuencia de las sumas después de 10,000 lanzamientos:")
print("-" * 50)
for suma, frecuencia in sorted(frecuencias_sumas.items()):
    print(f"Suma {suma}: {frecuencia} veces")
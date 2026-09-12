def calcular_total(lista_minerales):
    total_hierro = 0
    for mineral in lista_minerales:
        total_hierro += mineral
    return total_hierro

minerales = [15, 30, 8, 42]
resultado = calcular_total(minerales)
print(f"Total de hierro: {resultado}")
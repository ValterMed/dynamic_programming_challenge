def calcular_valores(casos):
    resultados = []
    for n, monedas in casos:
        valor_posible = set()
        for moneda in monedas:
            nuevo_valor = set(v + moneda for v in valor_posible)
            nuevo_valor.add(moneda)
            valor_posible |= nuevo_valor
        resultados.append(len(valor_posible))
    return resultados

casos = [
    (7, [3, 8, 1, 6, 4, 7, 3, 10]),
    (3, [8, 1, 10]),
    (3, [1, 3, 10])
]

print(calcular_valores(casos))

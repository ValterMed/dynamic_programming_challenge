def valores_posibles(t, casos):
    respuestas = []
    for i in range(t):
        n, monedas = casos[i]
        posibles = [0] * (sum(monedas) + 1)
        posibles[0] = 1
        for moneda in monedas:
            for j in range(len(posibles) - 1, -1, -1):
                if posibles[j]:
                    posibles[j + moneda] = 1
        respuestas.append(sum(posibles) - 1)
    return respuestas

# Ejemplo de uso
t = 3
casos = [
    (7, [8, 6, 4, 6, 7, 3, 10]),
    (3, [8, 1, 10]),
    (7, [1, 7, 3, 7, 2, 9, 8])
]
print(valores_posibles(t, casos))  # Output: [38, 7, 37]

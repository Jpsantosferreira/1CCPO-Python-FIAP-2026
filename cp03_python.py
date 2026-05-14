# SISTEMA: Monitoramento ambiental de salas

temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

limite_critico = 33

m_critico = 0
sala_mrisco = 0

for i, sala in enumerate(temperaturas):
    numero_sala = i + 1
    media = sum(sala) / len(sala)
    registros_criticos = sum(1 for temp in sala if temp >= limite_critico)

    print(f"Sala {numero_sala}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registros_criticos}")
    print()

    if registros_criticos > m_critico:
        m_critico = registros_criticos
        sala_mrisco = numero_sala

print(f"Sala com maior risco: Sala {sala_mrisco}")






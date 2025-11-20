# Función principal recursiva para la Multiplicación Rusa
def multiplicacion_rusa_recursiva(A, B, resultado_parcial=0):
    """
    Calcula la multiplicación A * B utilizando el método ruso de forma recursiva.

    Args:
        A (int): El primer número (dividendo).
        B (int): El segundo número (multiplicador).
        resultado_parcial (int): Acumulador del resultado de las sumas.

    Returns:
        int: El resultado final de A * B.
    """
    
    # 1. Caso Base: Cuando A llega a 1 (o 0 si se usa la condición de parada más estricta).
    # La recursión termina cuando la columna A llega a 1.
    if A == 0:
        return resultado_parcial
    
    # 2. Paso Recursivo: 
    
    # Determinar si A es impar
    es_impar = A % 2 != 0
    
    # **Impresión para visualizar el proceso (como en el ejemplo):**
    # Solo imprimimos si A es > 0, para no imprimir el caso base 0.
    if A > 0:
        print(f"{A:<10} {B:<10} ", end="")
        if es_impar:
            print(f"{B}")
        else:
            print("")
    
    # Si A es impar, sumamos B al resultado parcial
    if es_impar:
        resultado_parcial += B
        
    # Nueva llamada recursiva:
    # - A se divide por 2 (división entera: //)
    # - B se multiplica por 2 (si A es > 1)
    # - Se pasa el resultado_parcial actualizado
    return multiplicacion_rusa_recursiva(A // 2, B * 2, resultado_parcial)


# Función para ejecutar el ejemplo y mostrar el formato final
def ejecutar_multiplicacion_rusa(num1, num2):
    print(f"--- Multiplicación Rusa: {num1} x {num2} ---\n")
    print(f"A         B         Sumandos")
    
    # Llamada a la función recursiva
    resultado = multiplicacion_rusa_recursiva(num1, num2)
    
    print("\n" + "="*30)
    print(f"Resultado: {resultado}")
    print("="*30)


# Ejecución del ejemplo solicitado
ejecutar_multiplicacion_rusa(11, 33)

# Otros ejemplos para probar (opcional)
# ejecutar_multiplicacion_rusa(5, 12) # Resultado: 60
# ejecutar_multiplicacion_rusa(10, 4) # Resultado: 40

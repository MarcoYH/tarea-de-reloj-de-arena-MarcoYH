def reloj_de_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return ""
    
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    resultado = ""
    
    # Parte superior del reloj (triángulo decreciente) - m líneas
    for i in range(m):
        num_caracteres = 2 * (m - i) - 1
        num_espacios = i
        linea = " " * num_espacios + s * num_caracteres
        resultado += linea + "\n"
        print(linea)
    
    # Parte inferior del reloj (triángulo creciente) - m-1 líneas
    for i in range(2, m + 1):
        num_caracteres = 2 * i - 1
        num_espacios = m - i
        linea = " " * num_espacios + s * num_caracteres
        resultado += linea + "\n"
        print(linea)
    
    return resultado

"""
Ejercicios de Recursividad
Por: Keytlen Mata
"""

# ============================================
# 1. Suma de los n primeros números naturales
# ============================================
def suma_naturales(n: int) -> int:
    """
    Calcula la suma de los n primeros números naturales.
    Ejemplo: suma_naturales(5) = 1+2+3+4+5 = 15
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + suma_naturales(n - 1)


# ============================================
# 2. Imprimir números naturales entre a y d
# ============================================
def imprimir_rango(a: int, d: int) -> None:
    """
    Imprime los números naturales comprendidos entre a y d.
    Ejemplo: imprimir_rango(3, 7) → 3, 4, 5, 6, 7
    """
    if a > d:
        return
    print(a, end=" ")
    imprimir_rango(a + 1, d)


# ============================================
# 3. Cantidad de dígitos de un número entero
# ============================================
def contar_digitos(n: int) -> int:
    """
    Devuelve la cantidad de dígitos de un número entero.
    Ejemplo: contar_digitos(12345) = 5
    """
    n = abs(n)  # Manejar números negativos
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)


# ============================================
# 4. Calcular x^y mediante multiplicaciones sucesivas
# ============================================
def potencia(x: int, y: int) -> int:
    """
    Calcula x elevado a y mediante multiplicaciones sucesivas.
    Ejemplo: potencia(2, 4) = 2*2*2*2 = 16
    """
    if y == 0:
        return 1
    if y == 1:
        return x
    return x * potencia(x, y - 1)


# ============================================
# 5. Calcular x*y mediante sumas sucesivas
# ============================================
def multiplicacion(x: int, y: int) -> int:
    """
    Calcula x multiplicado por y mediante sumas sucesivas.
    Ejemplo: multiplicacion(4, 3) = 4+4+4 = 12
    """
    if y == 0:
        return 0
    if y < 0:
        return -multiplicacion(x, -y)
    return x + multiplicacion(x, y - 1)


# ============================================
# 6. Valor máximo de un vector recursivamente
# ============================================
def maximo_vector(vector: list, n: int = None) -> int:
    """
    Calcula el valor máximo de un vector recursivamente.
    Ejemplo: maximo_vector([3, 7, 2, 9, 4]) = 9
    """
    if n is None:
        n = len(vector)
    
    if n == 0:
        raise ValueError("El vector está vacío")
    if n == 1:
        return vector[0]
    
    max_resto = maximo_vector(vector, n - 1)
    return vector[n - 1] if vector[n - 1] > max_resto else max_resto


# ============================================
# 7. Contar secuencias de dos 1 seguidas en binario
# ============================================
def contar_dos_unos(cadena: str, pos: int = 0) -> int:
    """
    Cuenta el número de secuencias de dos 1 seguidas en una cadena binaria.
    Ejemplo: contar_dos_unos("110111") = 3 (posiciones: 0-1, 3-4, 4-5)
    """
    if pos >= len(cadena) - 1:
        return 0
    
    if cadena[pos] == '1' and cadena[pos + 1] == '1':
        return 1 + contar_dos_unos(cadena, pos + 1)
    else:
        return contar_dos_unos(cadena, pos + 1)


# ============================================
# 8. Convertir hexadecimal a decimal
# ============================================
def hex_a_decimal(cadena: str, longitud: int = None) -> int:
    """
    Convierte una cadena de dígitos hexadecimales a decimal.
    Ejemplo: hex_a_decimal("1A3") = 1*256 + 10*16 + 3 = 419
    """
    if longitud is None:
        longitud = len(cadena)
    
    if longitud == 0:
        return 0
    
    # Obtener el último dígito hexadecimal
    digito = cadena[longitud - 1].upper()
    valor = int(digito, 16)  # Convierte '0'-'9','A'-'F' a su valor decimal
    
    # Recursión: valor del último dígito + valor del resto * 16
    return valor + 16 * hex_a_decimal(cadena, longitud - 1)


# ============================================
# 9. Contar secuencias de m unos seguidos
# ============================================
def contar_m_unos(cadena: str, m: int, pos: int = 0) -> int:
    """
    Cuenta el número de secuencias de m unos seguidos en una cadena binaria.
    Ejemplo: contar_m_unos("1110111", 3) = 2 (dos secuencias de "111")
    """
    if pos > len(cadena) - m:
        return 0
    
    # Verificar si hay m unos seguidos desde la posición actual
    secuencia = cadena[pos:pos + m]
    if secuencia == '1' * m:
        return 1 + contar_m_unos(cadena, m, pos + 1)
    else:
        return contar_m_unos(cadena, m, pos + 1)


# ============================================
# 10. Calcular C(n,k) - Coeficiente binomial
# ============================================
def coeficiente_binomial(n: int, k: int) -> int:
    """
    Calcula el coeficiente binomial C(n,k) = n! / (k! * (n-k)!)
    Usando la fórmula recursiva: C(n,k) = C(n-1,k-1) + C(n-1,k)
    Casos base: C(n,0) = C(n,n) = 1
    
    Ejemplo: C(5,2) = 10
    """
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    
    return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)


# ============================================
# PROGRAMA DE PRUEBAS
# ============================================
def main():
    print("=" * 60)
    print("EJERCICIOS DE RECURSIVIDAD")
    print("=" * 60)
    
    # Ejercicio 1
    print("\n1. Suma de los n primeros números naturales:")
    n = 10
    print(f"   suma_naturales({n}) = {suma_naturales(n)}")
    
    # Ejercicio 2
    print("\n2. Números naturales entre a y d:")
    a, d = 5, 12
    print(f"   imprimir_rango({a}, {d}): ", end="")
    imprimir_rango(a, d)
    
    # Ejercicio 3
    print("\n\n3. Cantidad de dígitos de un número:")
    num = 12345
    print(f"   contar_digitos({num}) = {contar_digitos(num)}")
    
    # Ejercicio 4
    print("\n4. Potencia mediante multiplicaciones sucesivas:")
    x, y = 2, 8
    print(f"   potencia({x}, {y}) = {potencia(x, y)}")
    
    # Ejercicio 5
    print("\n5. Multiplicación mediante sumas sucesivas:")
    x, y = 7, 6
    print(f"   multiplicacion({x}, {y}) = {multiplicacion(x, y)}")
    
    # Ejercicio 6
    print("\n6. Valor máximo de un vector:")
    vector = [3, 7, 2, 9, 4, 11, 6]
    print(f"   maximo_vector({vector}) = {maximo_vector(vector)}")
    
    # Ejercicio 7
    print("\n7. Contar secuencias de dos 1 seguidas:")
    binario = "1101110011"
    print(f"   contar_dos_unos('{binario}') = {contar_dos_unos(binario)}")
    
    # Ejercicio 8
    print("\n8. Convertir hexadecimal a decimal:")
    hex_num = "1A3F"
    print(f"   hex_a_decimal('{hex_num}') = {hex_a_decimal(hex_num)}")
    print(f"   Verificación: {int(hex_num, 16)}")
    
    # Ejercicio 9
    print("\n9. Contar secuencias de m unos seguidos:")
    binario = "11101111011"
    m = 3
    print(f"   contar_m_unos('{binario}', {m}) = {contar_m_unos(binario, m)}")
    
    # Ejercicio 10
    print("\n10. Coeficiente binomial C(n,k):")
    n, k = 5, 2
    print(f"   C({n},{k}) = {coeficiente_binomial(n, k)}")
    print(f"   C(6,3) = {coeficiente_binomial(6, 3)}")
    print(f"   C(10,4) = {coeficiente_binomial(10, 4)}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
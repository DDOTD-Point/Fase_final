# Constantes para las posiciones en la matriz
POSICION_NOMBRE = 1
POSICION_STOCK_ACTUAL = 2
POSICION_STOCK_MINIMO = 3

#Matriz_Articulos(Código, Nombre, Stock Actual, Stock Mínimo)
matriz_articulos = [
    ["101", "Arroz", 12, 11],
    ["102", "Frijoles", 4, 6],
    ["103", "Lentejas", 8, 5],
    ["104", "Arbejas", 9, 10],
    ["105", "Garbanzos", 2, 6]
]

#Se define la función para calcular la cantidad a pedir
def faltantes(actual, minimo):
    """Devuelve la cantidad a pedir basándose en el stock."""
    if actual >= minimo:
        cantidad = 0
    else:
        cantidad = minimo - actual
    return cantidad

#Se define la función para revisar el stock
def stock_revisar(matriz):
    """Recorre la matriz e imprime la lista de artículos a solicitar."""
    print("=== LISTA DE ARTICULOS A SOLICITAR ===")
    
    #Se define la variable para controlar la fila actual y el total de filas en la matriz
    fila_actual = 0
    total_filas = len(matriz)
    
    while fila_actual < total_filas:
        #Se extraen los datos necesarios de la fila actual
        nombre = matriz[fila_actual][POSICION_NOMBRE]
        stock_actual = matriz[fila_actual][POSICION_STOCK_ACTUAL]
        stock_minimo = matriz[fila_actual][POSICION_STOCK_MINIMO]
        
        #Se llama a la función para hacer el cálculo
        pedido = faltantes(stock_actual, stock_minimo)
        
        #Se imprime el resultado si es necesario el solicitar algo faltante
        if pedido != 0:
            print(f"-> ¡ATENCION!: Solicitar {pedido} unidades de {nombre}")
        
        #Ciclo para pasar a la siguiente fila
        fila_actual += 1

#Se iinicia la revisión del stock
stock_revisar(matriz_articulos)

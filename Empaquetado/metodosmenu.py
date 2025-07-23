from paquetes import crear_paquete, crear_producto, lista_cambios,catalogo_productos, ALMACENES
from predeterminados import registros_a
from manejadorcvs import exportar_almacen_excel

def menu_crear_producto():
    print("\n--- CREAR NUEVO PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    
    try:
        precio = float(input("Precio: $"))
        peso = float(input("Peso (kg): "))
        stock = int(input("Stock inicial: "))
    except ValueError:
        print("Error: Debes introducir números válidos")
        return
    
    print("\nCategorías disponibles:")
    print("P - Paquete de prueba")
    print("F - Frágil") 
    print("X - No marcado")
    print("E - Eléctrico")
    print("VA - Forma de vida")
    
    categoria = input("Categoría (P/F/X/E/VA): ").upper()
    
    if categoria not in ["P", "F", "X", "E", "VA"]:
        print("Categoría no válida")
        return
    
    producto = crear_producto(nombre, precio, peso, categoria, stock)
    print(f"Producto '{nombre}' creado exitosamente")

def menu_crear_paquete():
    if not catalogo_productos:
        print("No hay productos en el catálogo. Crea un producto primero.")
        return
    
    print("\n--- CREAR PAQUETE ---")
    print("Productos disponibles:")
    for i, nombre in enumerate(catalogo_productos.keys(), 1):
        print(f"{i}. {nombre}")
    
    try:
        opcion = int(input("Selecciona el número del producto: ")) - 1
        nombres = list(catalogo_productos.keys())
        
        if 0 <= opcion < len(nombres):
            producto_elegido = catalogo_productos[nombres[opcion]]
            cantidad = int(input("Cantidad para el paquete: "))
            
            paquete = crear_paquete(cantidad, producto_elegido)
            
            print("\nAlmacenes disponibles:")
            for almacen in ALMACENES.keys():
                print(f"- {almacen}")
            
            almacen = input("¿En qué almacén guardar? (default: Almacen_principal): ").strip()
            if not almacen:
                almacen = "Almacen_principal"
            
            if almacen in ALMACENES:
                paquete.guardar_paquete(almacen)
                print(f"Paquete {paquete.id} creado y guardado en {almacen}")
            else:
                print("Almacén no válido")
        else:
            print("Opción no válida")
    except ValueError:
        print("Debes introducir un número válido")

def ver_catalogo():
    if not catalogo_productos:
        print("El catálogo está vacío")
        return
    
    print("\n--- CATÁLOGO DE PRODUCTOS ---")
    for nombre, producto in catalogo_productos.items():
        print(f"• {nombre}: ${producto.get_precio()} - Stock: {producto.stock} - Categoría: {producto.categoria}")
def ver_almacen():
    print("\nCONTENIDO DE ALMACENES")
    for nombre_almacen, paquetes in ALMACENES.items():
        print(f"\n{nombre_almacen}: {len(paquetes)} paquetes")
        if paquetes:
            for paquete in paquetes:
                print(f"  - {paquete.id}: {paquete.cantidad}x {paquete.contenido._nombre}")

def ver_historial_cambios():
    print("\n--- HISTORIAL DE CAMBIOS ---")
    if not lista_cambios:
        print("No hay cambios registrados aún")
    else:
        print(f"Total de cambios: {len(lista_cambios)}")
        for i, cambio in enumerate(lista_cambios, 1):
            print(f"{i}. {cambio}")

def ver_registros_completos():
    print("\n--- REGISTROS CON FECHAS ---")
    if not registros_a:
        print("No hay registros guardados aún")
        print("Los registros se crean automáticamente con las funciones")
        return
    
    print(f"Total de registros: {len(registros_a)}")
    for registro_id, registro in registros_a.items():
        fecha_simple = registro.fecha.strftime('%d/%m/%Y %H:%M')
        print(f"\n{registro_id} - {fecha_simple}")
        print(f"   Notas: {registro._notas_operador}")
        if registro.cambios:
            print("   Cambios:")
            for cambio in registro.cambios:
                print(f"     - {cambio}")
        else:
            print("   Sin cambios registrados")
    print("\n--- CONTENIDO DE ALMACENES ---")
    for nombre_almacen, paquetes in ALMACENES.items():
        print(f"\n{nombre_almacen}: {len(paquetes)} paquetes")
        if paquetes:
            for paquete in paquetes:
                print(f"  - {paquete.id}: {paquete.cantidad}x {paquete.contenido._nombre}")

def menu_exportar():
    print("\n--- EXPORTAR ALMACÉN ---")
    print("Almacenes disponibles:")
    for almacen in ALMACENES.keys():
        print(f"- {almacen}")
    
    almacen = input("¿Qué almacén exportar? (default: Almacen_principal): ").strip()
    if not almacen:
        almacen = "Almacen_principal"
    
    if almacen in ALMACENES:
        if ALMACENES[almacen]:
            exportar_almacen_excel(almacen)
        else:
            print(f"El almacén {almacen} está vacío")
    else:
        print("Almacén no válido")
# Funciones simples para borrar y editar

def borrar_producto():
    """Borra un producto del catálogo"""
    if not catalogo_productos:
        print("No hay productos para borrar")
        return
    
    print("Productos disponibles:")
    for nombre in catalogo_productos.keys():
        print(f"- {nombre}")
    
    nombre = input("¿Qué producto borrar?: ").strip()
    
    if nombre in catalogo_productos:
        del catalogo_productos[nombre]
        lista_cambios.append(f"Se borró el producto {nombre}")
        print(f"Producto '{nombre}' borrado")
    else:
        print("Producto no encontrado")

def borrar_paquete():
    """Borra un paquete de cualquier almacén"""
    # Mostramos todos los paquetes
    encontrados = False
    for almacen, paquetes in ALMACENES.items():
        if paquetes:
            if not encontrados:
                print("Paquetes disponibles:")
                encontrados = True
            for paquete in paquetes:
                print(f"- {paquete.id} ({almacen})")
    
    if not encontrados:
        print("No hay paquetes para borrar")
        return
    
    id_paquete = input("ID del paquete a borrar: ").strip()
    
    # Busca y borra el paquete
    for almacen, paquetes in ALMACENES.items():
        for paquete in paquetes:
            if paquete.id == id_paquete:
                paquetes.remove(paquete)
                lista_cambios.append(f"Se borró el paquete {id_paquete} del {almacen}")
                print(f"Paquete {id_paquete} borrado")
                return
    
    print("Paquete no encontrado")

def editar_producto():
    """Edita el precio o stock de un producto"""
    if not catalogo_productos:
        print("No hay productos para editar")
        return
    
    print("Productos disponibles:")
    for nombre, producto in catalogo_productos.items():
        print(f"- {nombre}: ${producto.precio}, Stock: {producto.stock}")
    
    nombre = input("¿Qué producto editar?: ").strip()
    
    if nombre not in catalogo_productos:
        print("Producto no encontrado")
        return
    
    producto = catalogo_productos[nombre]
    
    print("¿Qué cambiar?")
    print("1. Precio")
    print("2. Stock")
    
    opcion = input("Opción (1 o 2): ").strip()
    
    try:
        if opcion == "1":
            nuevo_precio = float(input(f"Nuevo precio (actual: ${producto.precio}): $"))
            producto.precio = nuevo_precio
            producto._precio = nuevo_precio
            lista_cambios.append(f"Se cambió el precio de {nombre} a ${nuevo_precio}")
            print("Precio actualizado")
            
        elif opcion == "2":
            nuevo_stock = int(input(f"Nuevo stock (actual: {producto.stock}): "))
            producto.stock = nuevo_stock
            lista_cambios.append(f"Se cambió el stock de {nombre} a {nuevo_stock}")
            print("Stock actualizado")
        else:
            print("Opción no válida")
            
    except ValueError:
        print("Valor no válido")


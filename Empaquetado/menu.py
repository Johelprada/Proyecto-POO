from metodosmenu import menu_crear_paquete, menu_crear_producto, ver_almacen,ver_catalogo, menu_exportar, ver_historial_cambios, editar_producto, ver_registros_completos, borrar_producto, borrar_paquete
def mostrar_menu():
    print("\n" + "="*40)
    print("    SISTEMA DE ALMACÉN v1.6.7")
    print("="*40)
    print("1. Crear nuevo producto")
    print("2. Crear paquete")
    print("3. Ver productos del catálogo")
    print("4. Ver contenido de almacén")
    print("5. Exportar almacén a Excel")
    print("6. Ver historial de cambios")
    print("7. Ver registros con fechas")
    print("8. Editar producto")
    print("9. Borrar producto")
    print("10. Borrar paquete")
    print("11. Salir")
    print("="*40)

def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción: ").strip()
            
            if opcion == "1":
                menu_crear_producto()
            elif opcion == "2":
                menu_crear_paquete()
            elif opcion == "3":
                ver_catalogo()
            elif opcion == "4":
                ver_almacen()
            elif opcion == "5":
                menu_exportar()
            elif opcion == "6":
                ver_historial_cambios()
            elif opcion == "7":
                ver_registros_completos()
            elif opcion == "8":
                editar_producto()
            elif opcion == "9":
                borrar_producto()
            elif opcion == "10":
                borrar_paquete()
            elif opcion == "11":
                print("¡Gracias por usar el sistema de almacén!")
                break
            else:
                print("Opción no válida")
                
            input("\nPresiona Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break


mostrar_menu()
main()

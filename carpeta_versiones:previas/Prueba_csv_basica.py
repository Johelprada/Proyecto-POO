import csv
#creamos una clase producto con la cual vamos a poder generar los datos a los cuales queremos enlistar
class Producto:
    def __init__(self, id, nombre, precio, categoria, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
#aqui se maneja el csv (tengo que estudiarla mas, no puedo solo seguir tutoriales)
class ManejadorCSV:
    def __init__(self):
        self.archivo = 'productos.csv'
    
    def crear_csv(self):
  # Aqui creamos los datos de prueba (se espera que estos datos al final sean los de la lista global osea el almacen principal)
        datos = [
            ['ID', 'Nombre', 'Precio', 'Categoria', 'Stock'],
            [1, 'computador', 850.99, 'Electronica', 15],
            [2, 'Mouse', 25.50, 'Accesorios', 50],
            [3, 'Teclado Mecanico', 89.99, 'Accesorios', 30],
            [4, 'Monitor 24"', 299.99, 'Electronica', 8],
            [5, 'Auriculares', 45.00, 'Audio', 25],
            [6, 'Teclado', 80.00, 'Electronica', 14]
        ]
        
        with open(self.archivo, 'w', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerows(datos)
        
        print(f"Archivo {self.archivo} creado")

    def leer_csv_basico(self):
        print("--- Lectura basica con CSV ---")
        try:
            with open(self.archivo, 'r') as f:
                lector = csv.reader(f)
                for fila in lector:
                    print(fila)
        except FileNotFoundError:
            print("Error: archivo no encontrado")
#definimos los filtros que se van a poner, aqui tome el atributo precio, pero en el proyecto final tmb podriamos usar cosas como urgente, vivo, etc.
    def probar_filtros(self):
        print("\n--- Productos caros (>$50) ---") #revisamos solo productos que valen mas de 50
        try:
            with open(self.archivo, 'r') as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    if float(fila['Precio']) > 50:
                        print(f"{fila['Nombre']} - ${fila['Precio']}")
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n--- Por categoria ---") # organizamos los productos por categoria
        try:
            with open(self.archivo, 'r') as f:
                lector = csv.DictReader(f)
                categorias = {}
                for fila in lector:
                    categoria = fila['Categoria']
                    precio = float(fila['Precio'])
                    
                    if categoria not in categorias:
                        categorias[categoria] = []
                    categorias[categoria].append(precio)
                
                for categoria, precios in categorias.items():
                    promedio = sum(precios) / len(precios)
                    print(f"{categoria}: ${promedio:.2f}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    print(" PRUEBA DE CSV ")
    
    manejador = ManejadorCSV()
    
    # Creamos el CSV
    manejador.crear_csv()
    
    # Leemos de forma basica
    manejador.leer_csv_basico()
    
    # Probar algunos filtros
    manejador.probar_filtros()

if __name__ == "__main__":
    main()

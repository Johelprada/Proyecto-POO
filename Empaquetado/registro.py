import pickle
from datetime import datetime
from paquetes import lista_cambios

class Registro:
    #TIPOS_R={"P":"Prueba","A":"General", "U":"Urgente" "X":"Trivial"} pruebas experimentales de id Registro
    N_registro=0
    def __init__(self, notas_operador: str, cambios: list = None, tipo:str="P"):
        self.fecha = datetime.now()  # Fecha y hora del registro
        Registro.N_registro += 1
        self.tipo = tipo
        self.id = f"{self.fecha.strftime('%m-%d-%H')}:{self.tipo}{Registro.N_registro:04}" #ID unico cada fecha
        self._notas_operador = notas_operador
        self.cambios = cambios if cambios else []  # Cambios realizados en listas u objetos
        registros_a[self.id] = self #clave para guardar los registros que se crean

    def mostrar_registro(self):
        print("=== Registro ===")
        print(f"ID de registro: {self.id}")
        print(f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Notas del operador: {self._notas_operador}")
        print("Cambios registrados:")
        if len(self.cambios) == 0:
            print("No hubo ningun cambio")
        else:
            for cambio in self.cambios:
                print(f"-{cambio}\n")
        print("================\n")

    def agregar_nota(self, nueva_nota: str):
        self._notas_operador += f"\n{nueva_nota}"

    def agregar_cambio(self, cambio: str):
        self.cambios.append(cambio)

    def __str__(self):
        return f'{self.id}: Usar "metodo mostrar_registro" para leer'

# Metodos para registros
def descargar():
    nombre_archivo = input("Que nombre le quieres poner a estos registros?: ")
    with open(f"{nombre_archivo}.pkl", "wb") as archivo:
        pickle.dump(registros_a, archivo)
def cargar(nombre_archivo="registros_p.pkl"):
    global registros_a
    with open(nombre_archivo, "rb") as archivo:
        registros_a = pickle.load(archivo)

def crear_registro(notas_op:str, tip:str)->"Registro": #Funcion escencial para generar registros
    New_R=Registro(notas_op, lista_cambios, tip)
    return New_R
import pickle
from datetime import datetime #Unicamente me interesa el datetime(class) no el modulo completo

lista_cambios = [] #Lista donde se guardaran los cambios generados por funciones def y metodos de clase
registros_a = {} #registros globales!
#Tipos de informe A:Generico , U:Importante P:De prueba
class Registro:
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


registro1=Registro("Hola wenas",[])
#registro1.mostrar_registro()
#print(f"{registro1.id} - {registro1.N_registro}\n")
registro2=Registro("Que mas!",["NO CAMBIA NADA"],"A")
#registro2.mostrar_registro()
#print(f"{registro2.id} - {registro2.N_registro}\n")
#registro3=Registro("Nota nueva!",[], "X")

#new_reg= crear_registro(input("Agrega tus notas aqui:"),"A")
#new_reg.mostrar_registro()
r1=input("Deseas descargar algo? y/n:")
if r1 == "y":
    descargar()

r=input("Deseas descargar algo? y/n:")
if r == "y":
    cargar()
print(registros_a)
cargar("registros_b.pkl")
print(registros_a)
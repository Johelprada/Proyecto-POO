from datetime import datetime #Unicamente me interesa el datetime(class) no el modulo completo

lista_cambios = [] #Lista donde se guardaran los cambios generados por funciones def y metodos de clase
REGISTROS = {} #registros globales!
#Tipos de informe A:Generico , U:Importante P:De prueba
class Registro:
    N_registro=0
    def __init__(self, notas_operador: str, cambios: list = None, tipo:str="P"):
        self.fecha = datetime.now()  # Fecha y hora del registro
        Registro.N_registro += 1
        self.tipo = tipo
        self.id = f"{self.fecha.strftime('%m-%d')}:{self.tipo}{Registro.N_registro:04}" #ID unico cada fecha
        self.notas_operador = notas_operador
        self.cambios = cambios if cambios else []  # Cambios realizados en listas u objetos
        REGISTROS[self.id] = self

    def mostrar_registro(self):
        print("=== Registro ===")
        print(f"ID de registro: {self.id}")
        print(f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Notas del operador: {self.notas_operador}")
        print("Cambios registrados:")
        if len(self.cambios) == 0:
            print("No hubo ningun cambio")
        else:
            for cambio in self.cambios:
                print(f"-{cambio}\n")
        print("================\n")

    def agregar_nota(self, nueva_nota: str):
        self.notas_operador += f"\n{nueva_nota}"

    def agregar_cambio(self, cambio: str):
        self.cambios.append(cambio)

def crear_registro(notas_op:str, tip:str)->"Registro": #Funcion escencial para generar registros
    New_R=Registro(notas_op, lista_cambios, tip)
    return New_R


registro1=Registro("Hola wenas",[])
registro1.mostrar_registro()
print(f"{registro1.id} - {registro1.N_registro}\n")
registro2=Registro("Que mas!",["NO CAMBIA NADA"],"A")
registro2.mostrar_registro()
print(f"{registro2.id} - {registro2.N_registro}\n")

new_reg= crear_registro(input("Agrega tus notas aqui:"),"A")
new_reg.mostrar_registro()

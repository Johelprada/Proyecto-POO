import pickle
from datetime import datetime #Unicamente me interesa el datetime(class) no el modulo completo

ALMACENES= { "Almacen_principal":[], "Almacen_2":[], "Almacen_3":[] }

catalogo_productos={}

lista_cambios = [] #Lista donde se guardaran los cambios generados por funciones def y metodos de clase

registros_a = {} #registros globales! y para descargar

#Tipos de informe A:Generico , U:Importante P:De prueba
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


class Producto:
    definition="Soy un elemento que clasificara con caracteristicas especificas"
    def __init__(self, nombre:str, precio:float, peso:float, categoria:str, stock:int):
        self._nombre = nombre
        self.precio = precio
        self.peso = peso
        self.categoria = categoria
        self.stock = stock
    def reavastecer(self, tantos:int):
        self.stock+=tantos

    def get_peso(self)->float:
        return self.peso

    def get_precio(self)->float:
        return self._precio
    def get_objeto(self)->str:
        return self._nombre
    def __str__(self)->str:
        return f"{self._contenido} con valor de {self._precio}$ por unidad"
  
guia_de_ids={
    "P":"es un paquete de prueba", 
    "F":"el paquete es Fragil" ,
    "X":"el paquete no fue marcado",
    "E":"el paquete es electrico",
    "VA":"el paquete posee una forma de vida"
    }

class Paquete:
    IDs_gen= {"P":0, "F":0 , "X":0, "E":0, "VA":0} #Diccionario permite escalabilidad de seriales!
    lista_de_cambios=[]
    def __init__(self, cantidad:int, contenido:"Producto"):
        #Serie de ID--------------------
        self.clasificado=contenido.categoria
        serial=Paquete.IDs_gen[self.clasificado]
        self.id= f"#{serial:04}{self.clasificado}"
        Paquete.IDs_gen[self.clasificado]= 0 if serial > 9999 else serial+=1
        #-------------------------------
        self.contenido=contenido._nombre
        self.cantidad=cantidad
        self._precio=contenido.get_precio()*self.cantidad
        self.peso=contenido.get_peso()*self.cantidad

    def esta_en_almacen(self, almacen:str)->bool:
        if self in ALMACENES[almacen]:
            return True
        else:
            return False
        
    def ver_contenido(self):
        lista_cambios.append(f"Se reviso el contenido del paquete {self.id}")
        return self.contenido
        
    def guardar_paquete(self, almacen:str):
        if self not in ALMACENES[almacen]:
            ALMACENES[almacen].append(self)
            lista_cambios.append(f"Se guardo el paquete {self.id} en el almacen {ALMACENES[almacen]}")
        else:
            print("El paquete ya esta en este almacen")

    def guardas_muchos_paquetes(self, almacen:list):
        for elemento in almacen:
            if elemento not in almacen:
                almacen.append(elemento)
            else:
                print(f"El paquete {elemento} ya este en el almacen")
        
    def es_fragil(self):
        return self.contenido.es_fragil()
    
    def __str__(self):
        return f"{self.id}"  #f"Paquete de {self.cantidad} x {self.contenido.contenido} ({'frágil' if self.contenido.es_fragil else 'no frágil'})"
    
#Metodos de paquetes y productos
def crear_producto(nombre:str, precio:float, peso:float, categoria:str, stock:int)->"Producto":
    mercancia=Producto(nombre, precio, peso, categoria, stock)
    catalogo_productos[nombre]=Producto
    lista_cambios.append(f"Se agrego el producto {nombre} al catagolo de mercancias con un precio de {precio}")
    return mercancia

def crear_paquete(cantidad:int, contenido:"Producto"):
    nuevo_paquete=Paquete(cantidad, contenido)
    lista_cambios.append(f"Se armo el paquete {nuevo_paquete.id}")
    return nuevo_paquete

#Prueba de impresion-------------------------------------
print("Deseas obtener la guia de ids de paquetes actual?")
solicitud_operador=input("Y/N:")
v = solicitud_operador.lower() == "y" #  tambien sirve v = True if solicitud_operador in ("Y", "y") else False

if v == True:
  for id , ref in guia_de_ids.items():
    print(f"{id}:{ref}\n")

#Pruebas Registro----------------------------------------
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
#---------------------------------------------------------
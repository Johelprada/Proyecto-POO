ALMACENES= { "Almacen_principal":[], "Almacen_2":[], "Almacen_3":[] }

catalogo_productos={}

lista_cambios = []

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
        Paquete.IDs_gen[self.clasificado]= 0 if serial > 9999 else serial
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
    

def crear_producto(nombre:str, precio:float, peso:float, categoria:str, stock:int)->"Producto":
    mercancia=Producto(nombre, precio, peso, categoria, stock)
    catalogo_productos[nombre]=Producto
    lista_cambios.append(f"Se agrego el producto {nombre} al catagolo de mercancias con un precio de {precio}")
    return mercancia

def crear_paquete(cantidad:int, contenido:"Producto"):
    nuevo_paquete=Paquete(cantidad, contenido)
    lista_cambios.append(f"Se armo el paquete {nuevo_paquete.id}")
    return nuevo_paquete
print("Deseas obtener la guia de ids de paquetes actual?")
solicitud_operador=input("Y/N:")
v = solicitud_operador.lower() == "y" #  tambien sirve v = True if solicitud_operador in ("Y", "y") else False

if v == True:
  for id , ref in guia_de_ids.items():
    print(f"{id}:{ref}\n")

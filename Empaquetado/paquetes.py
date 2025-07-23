from producto import Producto
from predeterminados import lista_cambios,catalogo_productos, ALMACENES

class Paquete:
    IDs_gen= {"P":0, "F":0 , "X":0, "E":0, "VA":0} #Diccionario permite escalabilidad de seriales!
    lista_de_cambios=[]
    def __init__(self, cantidad:int, contenido:"Producto"):
        #Serie de ID--------------------
        self.clasificado=contenido.categoria
        serial=Paquete.IDs_gen[self.clasificado]
        self.id= f"#{serial:04}{self.clasificado}"
        Paquete.IDs_gen[self.clasificado]= 0 if serial > 9999 else serial + 1
        #-------------------------------
        self.contenido=contenido
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
        return self.contenido._nombre
        
    def guardar_paquete(self, almacen:str):
        if self not in ALMACENES[almacen]:
            ALMACENES[almacen].append(self)
            lista_cambios.append(f"Se guardo el paquete {self.id} en el almacen {almacen}")
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
    catalogo_productos[nombre]=mercancia
    lista_cambios.append(f"Se agrego el producto {nombre} al catagolo de mercancias con un precio de {precio}")
    return mercancia

def crear_paquete(cantidad:int, contenido:"Producto"):
    nuevo_paquete=Paquete(cantidad, contenido)
    lista_cambios.append(f"Se armo el paquete {nuevo_paquete.id}")
    return nuevo_paquete

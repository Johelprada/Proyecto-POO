alamacen_principal=[] #Soy donde se almacenan los paquetes!
almacen_2=[] #Soy donde se almacenan los paquetes!
almacen_3=[] #Soy donde se almacenan los paquetes!

class Contenido:
    definition="Soy un elemento que clasificara con caracteristicas especificas"
    def __init__(self, contenido:str, precio_unidad:float, peso:float,es_fragil:bool=False):
        self._contenido=contenido
        self._precio=precio_unidad
        self.es_fragil=es_fragil
        self.peso= peso
    def get_precio(self):
        return self._precio
    def get_precio(self):
        return self._contenido
    def __str__(self):
        return f"Soy un {self._contenido} con valor de {self._precio} por unidad"
        
guia_de_ids={
    "P":"es un paquete de prueba", 
    "F":"el paquete es Fragil" ,
    "X":"el paquete no fue marcado",
    "E":"el paquete es electrico",
    "VA":"el paquete posee una forma de vida"
    }

class Paquete:
    # "P" Prueba "F"  "X" sin marcar "E" Electronico
    IDs_gen= {"P":0, "F":0 , "X":0, "E":0, "VA":0} #Diccionario permite escalabilidad de seriales!
    lista_de_cambios=[]
    def __init__(self, cantidad:int, contenido:"Contenido", clas:str):
        self.clasificado=clas
        serial=Paquete.IDs_gen[self.clasificado]
        self.id= f"#{serial:04}{self.clasificado}"
        Paquete.IDs_gen[self.clasificado]= 0 if serial > 9999 else serial+1
        self.contenido=contenido._contenido
        self.cantidad=cantidad
        self._precio=contenido._precio*self.cantidad
        self.peso=contenido.peso*self.cantidad

    def esta_en_almacen(self, almacen:list)->bool:
        if self in almacen:
            return True
        else:
            return False
        
    def guardar_paquete(self, almacen:list):
        if self not in almacen:
            almacen.append(self)
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
        return f"Paquete de {self.cantidad} x {self.contenido.contenido} ({'frágil' if self.contenido.es_fragil else 'no frágil'})"
print("Deseas obtener la guia de ids de paquetes actual?")
solicitud_operador=input("Y/N:")
v = v = True if solicitud_operador in ("Y", "y") else False # v = solicitud_operador.lower() == "y" tambien sirve

if v == True:
  for id , ref in guia_de_ids.items():
    print(f"{id}:{ref}\n")

# Proyecto-POO
## Borrador

```python
almacen_principal=[] #Soy donde se almacenan los paquetes!
almacen_2=[] #Soy donde se almacenan los paquetes!
almacen_3=[] #Soy donde se almacenan los paquetes!
registros=[]
class Registro:
    pass
class Contenido:
    definition="Soy un elemento que clasificara con caracteristicas especificas"
    def __init__(self, contenido:str, es_fragil:bool):
        self.contenido=contenido
        self.es_fragil=es_fragil
    def __str__(self):
        return f"Soy un {self.contenido}"
        

class Paquete:
    def __init__(self, cantidad:int, peso:float, contenido:"Contenido"):
        self.contenido=contenido
        self.cantidad=cantidad
        self.peso=peso

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
        return self.contenido.es_fragil
    
    def __str__(self):
        return f"Paquete de {self.cantidad} x {self.contenido.contenido} ({'frágil' if self.contenido.es_fragil else 'no frágil'})"
```

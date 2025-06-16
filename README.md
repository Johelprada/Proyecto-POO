# Proyecto-POO
## Borrador

```python
almacen_principal=[] #Soy donde se almacenan los paquetes!
almacen_2=[] #Soy donde se almacenan los paquetes!
almacen_3=[] #Soy donde se almacenan los paquetes!
registros=[]

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
# Clase Registro
```python
from datetime import datetime #Unicamente me interesa el datetime(class) no el modulo completo
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

registro1=Registro("Hola wenas",[])
registro1.mostrar_registro()
print(f"{registro1.id} - {registro1.N_registro}\n")
registro2=Registro("Que mas!",["NO CAMBIA NADA"],"A")
registro2.mostrar_registro()
print(f"{registro2.id} - {registro2.N_registro}\n")
```

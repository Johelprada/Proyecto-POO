class Producto:
    definition="Soy un elemento que clasificara con caracteristicas especificas"
    def __init__(self, nombre:str, precio:float, peso:float, categoria:str, stock:int):
        self._nombre = nombre
        self._precio = precio
        self._contenido = nombre
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
    
    def es_fragil(self)->bool:
        return self.categoria == "F"
    
    def __str__(self)->str:
        return f"{self._contenido} con valor de {self._precio}$ por unidad"
  
guia_de_ids={
    "P":"es un paquete de prueba", 
    "F":"el paquete es Fragil" ,
    "X":"el paquete no fue marcado",
    "E":"el paquete es electrico",
    "VA":"el paquete posee una forma de vida"
    }

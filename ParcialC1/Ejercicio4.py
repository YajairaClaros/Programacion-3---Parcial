"""Una empresa cuenta con dos tipos de empleados: aquellos con plaza
fija y aquellos que trabajan por horas. Se han registrado los datos de
ambos tipos y, al generar la planilla de pago, se realizan dos cálculos
diferentes. A los empleados de plaza fija se les paga el salario base más
comisiones, mientras que a los empleados por horas se les paga en
función de la cantidad de horas trabajadas.
 Adicionalmente, si un empleado ha laborado más de 5 años, sin
importar su tipo de contrato, se le otorga un bono adicional.
Implemente esto en su código.
"""
# ABC (Abstract Base Class) se usa para crear clases abstractas
# abstractmethod es un decorador para métodos abstractos
from abc import ABC, abstractmethod

# Definición de la clase abstracta Empleado
class Empleado(ABC):
    def __init__(self, nombre, años_trabajados):
        # Constructor de la clase Empleado
        self.nombre = nombre
        self.años_trabajados = años_trabajados

    @abstractmethod
    def calcular_salario(self):
        # Método abstracto que debe ser implementado por las clases hijas
        pass

    def aplicar_bono_antiguedad(self, salario):
        # Método para aplicar el bono de antigüedad
        if self.años_trabajados > 5:
            bono = salario * 0.1
            return salario * 1.1, bono  # Retorna el salario con bono y el monto del bono
        return salario, 0  # Si no hay bono, retorna el salario original y 0 como bono

# Clase para empleados de plaza fija
class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, años_trabajados, salario_base, comisiones):
        # Constructor de la clase EmpleadoPlazaFija
        super().__init__(nombre, años_trabajados)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_salario(self):
        # Cálculo del salario para empleados de plaza fija
        salario = self.salario_base + self.comisiones
        return self.aplicar_bono_antiguedad(salario)

# Clase para empleados por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, años_trabajados, horas_trabajadas, tarifa_por_hora):
        # Constructor de la clase EmpleadoPorHoras
        super().__init__(nombre, años_trabajados)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        # Cálculo del salario para empleados por horas
        salario = self.horas_trabajadas * self.tarifa_por_hora
        return self.aplicar_bono_antiguedad(salario)

# Función para obtener datos del usuario
def obtener_datos_empleado():
    # Solicita y retorna los datos del empleado ingresados por el usuario
    nombre = input("Ingrese el nombre del empleado: ")
    años_trabajados = int(input("Ingrese los años trabajados: "))
    tipo_empleado = input("¿Es empleado de plaza fija (F) o por horas (H)? ").upper()
    
    if tipo_empleado == 'F':
        salario_base = float(input("Ingrese el salario base: "))
        comisiones = float(input("Ingrese las comisiones: "))
        return EmpleadoPlazaFija(nombre, años_trabajados, salario_base, comisiones)
    elif tipo_empleado == 'H':
        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
        tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
        return EmpleadoPorHoras(nombre, años_trabajados, horas_trabajadas, tarifa_por_hora)
    else:
        print("Tipo de empleado no válido.")
        return None

# Programa principal
if __name__ == "__main__":
    # Bloque principal del programa
    while True:
        # Obtiene los datos del empleado
        empleado = obtener_datos_empleado()
        if empleado:
            # Calcula el salario y el bono del empleado
            salario_total, bono = empleado.calcular_salario()
            
            print(f"\nDetalles del empleado {empleado.nombre}:")
            if isinstance(empleado, EmpleadoPorHoras):
                print(f"Tipo: Empleado por horas")
                print(f"Horas trabajadas: {empleado.horas_trabajadas}")
                print(f"Tarifa por hora: ${empleado.tarifa_por_hora:.2f}")
                print(f"Salario base: ${empleado.horas_trabajadas * empleado.tarifa_por_hora:.2f}")
            elif isinstance(empleado, EmpleadoPlazaFija):
                print(f"Tipo: Empleado de plaza fija")
                print(f"Salario base: ${empleado.salario_base:.2f}")
                print(f"Comisiones: ${empleado.comisiones:.2f}")
            
            if bono > 0:
                print(f"Bono de antigüedad: ${bono:.2f}")
            else:
                print("No aplica bono de antigüedad")
            
            print(f"Salario total: ${salario_total:.2f}")
        
        # Pregunta si se desea calcular otro salario
        continuar = input("\n¿Desea calcular otro salario? (S/N): ").upper()
        if continuar != 'S':
            break

    print("Programa finalizado.")
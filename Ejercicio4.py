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

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, años_trabajados):
        self.nombre = nombre
        self.años_trabajados = años_trabajados

    @abstractmethod
    def calcular_salario(self):
        pass

    def aplicar_bono_antiguedad(self, salario):
        if self.años_trabajados > 5:
            return salario * 1.1  # 10% de bono por antigüedad
        return salario

class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, años_trabajados, salario_base, comisiones):
        super().__init__(nombre, años_trabajados)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_salario(self):
        salario = self.salario_base + self.comisiones
        return self.aplicar_bono_antiguedad(salario)

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, años_trabajados, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, años_trabajados)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        salario = self.horas_trabajadas * self.tarifa_por_hora
        return self.aplicar_bono_antiguedad(salario)

# Ejemplo de uso
empleado1 = EmpleadoPlazaFija("Juan Pérez", 7, 2000, 500)
empleado2 = EmpleadoPorHoras("María García", 3, 160, 15)

print(f"Salario de {empleado1.nombre}: ${empleado1.calcular_salario():.2f}")
print(f"Salario de {empleado2.nombre}: ${empleado2.calcular_salario():.2f}")
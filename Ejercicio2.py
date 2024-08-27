""""Un colegio privado desea registrar la asistencia de sus estudiantes a las
clases cada docente tiene su listado de los estudiantes en los cuáles se
les ha solicitado colocar a la par de cada estudiante si ha asistido, si
cuenta con permiso o tiene inasistencia con la fecha respectiva.
Actualmente esto se maneja por unas hojas de papel impreso y se
entregan al director al final del día; la escuela necesita agilizar este
proceso.
 Si el estudiante tiene un permiso el director necesita la razón de
dicha falta, ¿Cómo solventarías esta situación? Agrega tu
propuesta al código."""

from datetime import date #Esta herramienta, nos ayudara a tomar el dato de fecha de una manera mas exacta

class Estudiante:#Toma los datos del estudiante
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = []

class Asistencia: #Toma los datos para la asistencia del estudiante
    def __init__(self, fecha, estado, razon=None):
        self.fecha = fecha
        self.estado = estado
        self.razon = razon

class SistemaAsistencia: #Tiene la lista de los estudiantes y puede contener los agregados
    #Esta funcion nos muestra una lista previa de estudiantes
    def __init__(self):
        self.estudiantes = [
            Estudiante("Juan Pérez"),
            Estudiante("María López"),
            Estudiante("Carlos Rodríguez")
        ]

    def agregar_estudiante(self, nombre):
        #esta funcion nos agrega estudiantes, a la lista de easitencia, si asi lo deseamos
        self.estudiantes.append(Estudiante(nombre))
        print(f"Estudiante {nombre} agregado con éxito.")
        #esta funcion nos ayuda a registrar la sisitencia de los estudiantes de la lista
    def registrar_asistencia(self, estudiante, estado, razon=None):
        fecha_actual = date.today()
        asistencia = Asistencia(fecha_actual, estado, razon)
        estudiante.asistencias.append(asistencia)
        #esta funcion nos muestra las asistencias tomadas
    def ver_asistencias(self):
        for estudiante in self.estudiantes:
            print(f"\nAsistencias de {estudiante.nombre}:")
            for asistencia in estudiante.asistencias:
                fecha = asistencia.fecha.strftime("%d/%m/%Y")
                if asistencia.estado == "permiso":
                    print(f"  {fecha}: {asistencia.estado} - Razón: {asistencia.razon}")
                else:
                    print(f"  {fecha}: {asistencia.estado}")

"""esta funcion le muestra un menu al usuario, para que el pueda tomar la asistencia, 
ver la asistencia, e incluso agregar un nuevo estudiante y si no es ninguna de las anteriores, 
salir del programa"""
def menu_principal():
    sistema = SistemaAsistencia()
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar asistencia")
        print("2. Ver asistencias")
        print("3. Agregar estudiante")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Registrar asistencia
            print("\nEstudiantes disponibles:")
            for i, estudiante in enumerate(sistema.estudiantes):
                print(f"{i+1}. {estudiante.nombre}")
            indice = int(input("Seleccione el número del estudiante: ")) - 1
            estudiante = sistema.estudiantes[indice]

            print("\nEstados de asistencia:")
            print("1. Asistió")
            print("2. Permiso")
            print("3. Inasistencia")
            estado_opcion = input("Seleccione el estado de asistencia: ")

            if estado_opcion == "1":
                sistema.registrar_asistencia(estudiante, "asistió")
            elif estado_opcion == "2":
                razon = input("Ingrese la razón del permiso: ")
                sistema.registrar_asistencia(estudiante, "permiso", razon)
            elif estado_opcion == "3":
                sistema.registrar_asistencia(estudiante, "inasistencia")
            else:
                print("Opción no válida.")
                continue

            print("Asistencia registrada con éxito.")

        elif opcion == "2":
            # Ver asistencias
            sistema.ver_asistencias()

        elif opcion == "3":
            # Agregar estudiante
            nombre = input("Ingrese el nombre del nuevo estudiante: ")
            sistema.agregar_estudiante(nombre)

        elif opcion == "4":
            # Salir
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
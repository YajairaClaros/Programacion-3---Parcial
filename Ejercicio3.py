# Clase que representa una habitación en el hotel
class Habitacion:
    def __init__(self, tipo, precio_por_noche):
        self.tipo = tipo  
        self.precio_por_noche = precio_por_noche  #

    # Método para mostrar la información de la habitación
    def mostrar_datos(self):
        print(f"Tipo de Habitación: {self.tipo}")
        print(f"Precio por Noche: ${self.precio_por_noche:.2f}")

# Clase que representa un cliente en el hotel
class Cliente:
    def __init__(self, nombre, noches, servicios_extra):
        self.nombre = nombre  
        self.noches = noches 
        self.servicios_extra = servicios_extra 

# Clase que gestiona el hotel y las reservas
class Hotel:
    def __init__(self):
        # Lista de habitaciones disponibles en el hotel
        self.habitaciones = [
            Habitacion("Simple", 50),
            Habitacion("Doble", 100),
            Habitacion("Suite", 200)
        ]
        # Costos adicionales por servicios extra
        self.costos_servicios_extra = {
            "piscina": 15,
            "cancha de golf": 30
        }

    # Método para mostrar las opciones de habitaciones
    def mostrar_opciones_habitaciones(self):
        print("*******************************")
        print("Opciones de Habitaciones:")
        
        for i, habitacion in enumerate(self.habitaciones):
            print(f"{i + 1}.", end=" ")
            habitacion.mostrar_datos()

    # Método para seleccionar una habitación
    def seleccionar_habitacion(self, opcion):
        if 1 <= opcion <= len(self.habitaciones):
            return self.habitaciones[opcion - 1]
        else:
            print("Opción inválida.")
            return None

    # Método para solicitar datos del cliente y generar factura
    def realizar_reserva(self):
        self.mostrar_opciones_habitaciones()

        # Solicita al usuario que elija una habitación
        opcion = int(input("Seleccione el número de la habitación deseada: "))
        habitacion_seleccionada = self.seleccionar_habitacion(opcion)
        if habitacion_seleccionada is None:
            return 
        
        # Solicita datos del cliente
        print("*********************")
        print("DATOS DEL CLIENTE")
        print("*********************")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        noches = int(input("Ingrese el número de noches que permanecerá: "))

        # Solicita servicios extra
        servicios_extra = []
        print("Servicios extra disponibles: piscina ($15) y cancha de golf ($30)")
        while True:
            servicio = input("Ingrese un servicio extra solicitado (o 'n' para finalizar): ").lower()
            if servicio == 'n':
                break
            elif servicio in self.costos_servicios_extra:
                servicios_extra.append(servicio)
            else:
                print("Servicio no disponible. Intente de nuevo.")

        # Calcula el costo total
        costo_habitacion = habitacion_seleccionada.precio_por_noche * noches
        costo_servicios_extra = sum(self.costos_servicios_extra[servicio] for servicio in servicios_extra)
        total = costo_habitacion + costo_servicios_extra

        # Muestra la factura
        print("------------------------")
        print("\nFactura Detallada")
        print("------------------------")
        print(f"Cliente: {nombre_cliente}")
        print(f"Tipo de Habitación: {habitacion_seleccionada.tipo}")
        print(f"Número de Noches: {noches}")
        print(f"Costo de Habitación: ${costo_habitacion:.2f}")
        if servicios_extra:
            print("Servicios Extra Solicitados:")
            for servicio in servicios_extra:
                print(f"  - {servicio.capitalize()}: ${self.costos_servicios_extra[servicio]:.2f}")
        else:
            print("No se solicitaron servicios extra.")
        print(f"Costo Total: ${total:.2f}")
        print("*********************")

# Clase para la interfaz de usuario
class InterfazHotel:
    def __init__(self):
        self.hotel = Hotel()  # Instancia de la clase Hotel

    # Método para iniciar la interfaz
    def iniciar(self):
        while True:
            print("\nOpciones:")
            print("1. Realizar una reserva")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.hotel.realizar_reserva()
            elif opcion == '2':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

# Inicia la interfaz del hotel
interfaz = InterfazHotel()
interfaz.iniciar()

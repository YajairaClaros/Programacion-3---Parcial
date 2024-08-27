# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, nombre, cantidad, precio_compra):
        #Los atributos del producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    # Método para calcular el precio de venta con un margen del 55%
    def calcular_precio_venta(self):
        return self.precio_compra * 1.55

    # Método para mostrar la información del producto
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")
        print("*******************************")

# Clase que gestiona el inventario de productos en la tienda
class Inventario:
    def __init__(self):
        self.productos = []  # Lista que almacena los productos registrados

    # Metodo para agregar un nuevo producto si niña Mary lo desea 
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado exitosamente.")

    # Metodo para mostrar todos los productos del incentario 
    def mostrar_inventario(self):
        print("---------------------------------------")
        print("       IVENTARIO DE PRODUCTOS")
        print("---------------------------------------")
        if not self.productos:
            print("No hay productos en el inventario.")
        for producto in self.productos:
            producto.mostrar_datos() # Muestra los datos de cada producto

# Clase que representa la tienda y gestiona las ventas y el iventario 
class Tienda:
    def __init__(self):
        self.inventario = Inventario()  # Instancia de la clase Inventario

    # Metodo para registrar un nuevo producto en la tienda
    def registrar_producto(self):
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad recibida: "))
        precio_compra = float(input("Precio de compra del producto: "))
        producto = Producto(nombre, cantidad, precio_compra)
        self.inventario.agregar_producto(producto)

    # Método para realizar una compra y calcular el total a pagar
    def realizar_compra(self):
        total = 0             # Variable para acumular el total de la compra
        while True:
            nombre = input("Nombre del producto a comprar (o 'salir' para finalizar): ")
            if nombre.lower() == 'salir':
                break
            cantidad = int(input("Cantidad a comprar: "))
            for producto in self.inventario.productos:
                if producto.nombre == nombre:
                    if producto.cantidad >= cantidad:
                        total += producto.precio_venta * cantidad
                        producto.cantidad -= cantidad
                        print(f"Producto '{nombre}' agregado a la compra.")
                    else:
                        print(f"Cantidad insuficiente de '{nombre}'.")
        
        if total > 0:
            print(f"Total a pagar: ${total:.2f}")
            while True:
                pago = float(input("Ingrese el monto con el que paga el cliente: "))
                if pago >= total:
                    vuelto = pago - total
                    print(f"Vuelto: ${vuelto:.2f}")
                    print("Gracias por su compra.")
                    break
                else:
                    print(f"El monto ingresado es insuficiente. El total es ${total:.2f}. Por favor, ingrese un monto mayor.")

# Clase que proporciona una interfaz para interactuar con la tienda
class InterfazTienda:
    def __init__(self):
        self.tienda = Tienda()

    def iniciar(self):
        # Menú de opciones para el usuario
        while True:
            print("\nOpciones:")
            print("1. Registrar un nuevo producto")
            print("2. Mostrar inventario")
            print("3. Realizar una compra")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.tienda.registrar_producto()
            elif opcion == '2':
                self.tienda.inventario.mostrar_inventario()
            elif opcion == '3':
                self.tienda.realizar_compra()
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")


# Iniciar la interfaz de la tienda
interfaz = InterfazTienda()
interfaz.iniciar()

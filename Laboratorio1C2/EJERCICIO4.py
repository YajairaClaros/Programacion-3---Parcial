import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
)

class MainVentana(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 400, 400)  
        self.setWindowTitle("Ejercicio 4 - Datos de Mascotas")

        # Crear un widget central
        central = QWidget(self)
        self.setCentralWidget(central)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Configuración para 3 mascotas
        self.mascotas = []
        for i in range(1, 4):
            self.agregar_formulario_mascota(layout, i)

        # Botón para confirmar y leer los datos ingresados
        self.confirmar_datos_btn = QPushButton("Confirmar Datos")
        self.confirmar_datos_btn.clicked.connect(self.confirmar_datos)

        # Etiqueta para mostrar el resultado
        self.resultado_label = QLabel("")

        # Añadir el botón y la etiqueta al layout
        layout.addWidget(self.confirmar_datos_btn)
        layout.addWidget(self.resultado_label)

        # Asignar el layout al widget central
        central.setLayout(layout)

    # Función para agregar el formulario de cada mascota
    def agregar_formulario_mascota(self, layout, numero):
        mascota_label = QLabel(f"Mascota {numero}")
        
        # Campos de entrada
        nombre_input = QLineEdit()
        nombre_input.setPlaceholderText("Nombre de la mascota")
        
        edad_input = QLineEdit()
        edad_input.setPlaceholderText("Edad de la mascota")
        
        tipo_input = QLineEdit()
        tipo_input.setPlaceholderText("Tipo de animal (ej: perro, gato)")
        
        # Añadir los widgets al layout
        layout.addWidget(mascota_label)
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(nombre_input)
        layout.addWidget(QLabel("Edad:"))
        layout.addWidget(edad_input)
        layout.addWidget(QLabel("Tipo:"))
        layout.addWidget(tipo_input)
        
        # Guardar referencias a los inputs de cada mascota
        self.mascotas.append((nombre_input, edad_input, tipo_input))

    # Función para confirmar los datos ingresados
    def confirmar_datos(self):
        resultados = []
        for i, (nombre_input, edad_input, tipo_input) in enumerate(self.mascotas, start=1):
            nombre = nombre_input.text()
            edad = edad_input.text()
            tipo = tipo_input.text()
            
            if nombre and edad and tipo:
                resultados.append(f"Mascota {i} - Nombre: {nombre}, Edad: {edad} años, Tipo: {tipo}")
            else:
                resultados.append(f"Mascota {i} - Faltan datos")

        # Mostrar los resultados en la etiqueta
        self.resultado_label.setText("\n".join(resultados))


app = QApplication(sys.argv)
ventana = MainVentana()
ventana.show()
app.exec()


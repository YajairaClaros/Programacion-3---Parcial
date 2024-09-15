import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
)

class MainVentana(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 400, 300) 
        self.setWindowTitle("Ejercicio 1")

        # Crear un widget central
        central = QWidget(self)
        self.setCentralWidget(central)

        # Crear un layout vertical
        self.layout = QVBoxLayout()

        # Etiquetas y campos de entrada
        self.nombre_label = QLabel("Ingrese su nombre:")
        self.nombre_input = QLineEdit()

        self.edad_label = QLabel("Ingrese su edad:")
        self.edad_input = QLineEdit()

        # Botón para mostrar los datos ingresados
        self.mostrar_datos_btn = QPushButton("Mostrar Datos")
        self.mostrar_datos_btn.clicked.connect(self.mostrar_datos)

        # Etiqueta para mostrar el resultado
        self.resultado_label = QLabel("")

        # Botón para reiniciar y permitir ingresar nuevos datos
        self.ingresar_otros_btn = QPushButton("Ingresar otros datos")
        self.ingresar_otros_btn.setVisible(False)  # No visible al inicio
        self.ingresar_otros_btn.clicked.connect(self.ingresar_nuevos_datos)

        # Añadir los widgets al layout
        self.layout.addWidget(self.nombre_label)
        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(self.edad_label)
        self.layout.addWidget(self.edad_input)
        self.layout.addWidget(self.mostrar_datos_btn)
        self.layout.addWidget(self.resultado_label)
        self.layout.addWidget(self.ingresar_otros_btn)

        # Asignar el layout al widget central
        central.setLayout(self.layout)

    # Función para mostrar los datos ingresados
    def mostrar_datos(self):
        nombre = self.nombre_input.text()
        edad = self.edad_input.text()

        if nombre and edad:
            self.resultado_label.setText(f"Nombre: {nombre}\nEdad: {edad} años")
            # Hacer el botón "Ingresar otros datos" visible
            self.ingresar_otros_btn.setVisible(True)
            # Desactivar los campos de entrada y el botón de mostrar datos
            self.nombre_input.setEnabled(False)
            self.edad_input.setEnabled(False)
            self.mostrar_datos_btn.setEnabled(False)
        else:
            self.resultado_label.setText("Por favor, ingrese ambos datos.")

    # Función para permitir al usuario ingresar nuevos datos
    def ingresar_nuevos_datos(self):
        # Limpiar los campos de texto y el resultado
        self.nombre_input.clear()
        self.edad_input.clear()
        self.resultado_label.setText("")
        # Volver a habilitar los campos y el botón de mostrar datos
        self.nombre_input.setEnabled(True)
        self.edad_input.setEnabled(True)
        self.mostrar_datos_btn.setEnabled(True)
        # Ocultar el botón "Ingresar otros datos"
        self.ingresar_otros_btn.setVisible(False)

app = QApplication(sys.argv)
ventana = MainVentana()
ventana.show()
app.exec()

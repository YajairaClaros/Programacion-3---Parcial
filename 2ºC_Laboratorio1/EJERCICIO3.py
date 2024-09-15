import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
)

class MainVentana(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 350, 250)  
        self.setWindowTitle("Ejercicio 3")

        # Crear un widget central
        central = QWidget(self)
        self.setCentralWidget(central)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Etiqueta y campo de entrada para el número de cédula
        self.cedula_label = QLabel("Ingrese su número de cédula:")
        self.cedula_input = QLineEdit()

        # Etiqueta y campo de entrada para el nombre completo
        self.nombre_label = QLabel("Ingrese su nombre completo:")
        self.nombre_input = QLineEdit()

        # Botón para confirmar y leer los datos ingresados
        self.confirmar_datos_btn = QPushButton("Confirmar Datos")
        self.confirmar_datos_btn.clicked.connect(self.confirmar_datos)

        # Etiqueta para mostrar el resultado
        self.resultado_label = QLabel("")

        # Añadir los widgets al layout
        layout.addWidget(self.cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.confirmar_datos_btn)
        layout.addWidget(self.resultado_label)

        # Asignar el layout al widget central
        central.setLayout(layout)

    # Función para confirmar los datos ingresados
    def confirmar_datos(self):
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()

        if cedula and nombre:
            self.resultado_label.setText(f"Cédula: {cedula}\nNombre: {nombre}")
        else:
            self.resultado_label.setText("Por favor, complete ambos campos.")

app = QApplication(sys.argv)
ventana = MainVentana()
ventana.show()
app.exec()

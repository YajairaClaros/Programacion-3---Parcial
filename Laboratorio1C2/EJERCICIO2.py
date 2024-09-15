import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
)

class MainVentana(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 400, 200)  
        self.setWindowTitle("Ejercicio 2")

        # Crear un widget central
        central = QWidget(self)
        self.setCentralWidget(central)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Etiqueta y campo de entrada para la clave secreta
        self.clave_label = QLabel("Ingrese su clave secreta:")
        self.clave_input = QLineEdit()
        self.clave_input.setEchoMode(QLineEdit.Password)  # Oculta los caracteres

        # Botón para confirmar la clave ingresada
        self.confirmar_clave_btn = QPushButton("Confirmar Clave")
        self.confirmar_clave_btn.clicked.connect(self.confirmar_clave)

        # Etiqueta para notificar el estado
        self.resultado_label = QLabel("")

        # Añadir los widgets al layout
        layout.addWidget(self.clave_label)
        layout.addWidget(self.clave_input)
        layout.addWidget(self.confirmar_clave_btn)
        layout.addWidget(self.resultado_label)

        # Asignar el layout al widget central
        central.setLayout(layout)

    # Función para confirmar la clave ingresada
    def confirmar_clave(self):
        clave = self.clave_input.text()

        if clave:
            self.resultado_label.setText("Clave ingresada correctamente.")
        else:
            self.resultado_label.setText("Por favor, ingrese una clave.")

app = QApplication(sys.argv)
ventana = MainVentana()
ventana.show()
app.exec()


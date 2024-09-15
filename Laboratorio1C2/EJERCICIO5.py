import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QComboBox
)

class MainVentana(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 400, 500)  # Posición y tamaño de la ventana
        self.setWindowTitle("Ejercicio 5 - Datos de la Persona")

        # Crear un widget central
        central = QWidget(self)
        self.setCentralWidget(central)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Crear etiquetas y campos de entrada para los 10 datos
        self.datos_persona = []
        self.agregar_campo(layout, "Nombre")
        self.agregar_campo(layout, "Apellido")
        self.agregar_campo(layout, "Edad")
        self.agregar_campo(layout, "Dirección")
        self.agregar_campo(layout, "Ciudad")
        self.agregar_campo(layout, "Teléfono")
        self.agregar_campo(layout, "Correo Electrónico")
        self.agregar_campo(layout, "Ocupación")
        self.agregar_campo(layout, "Nacionalidad")
        self.agregar_combo(layout, "Género", ["Masculino", "Femenino", "Otro"])

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

    # Función para agregar un campo de entrada con una etiqueta
    def agregar_campo(self, layout, etiqueta):
        label = QLabel(f"Ingrese {etiqueta}:")
        input_field = QLineEdit()
        input_field.setPlaceholderText(f"{etiqueta}")
        layout.addWidget(label)
        layout.addWidget(input_field)
        self.datos_persona.append((etiqueta, input_field))

    # Función para agregar un combo box con opciones
    def agregar_combo(self, layout, etiqueta, opciones):
        label = QLabel(f"Seleccione {etiqueta}:")
        combo_box = QComboBox()
        combo_box.addItems(opciones)
        layout.addWidget(label)
        layout.addWidget(combo_box)
        self.datos_persona.append((etiqueta, combo_box))

    # Función para confirmar los datos ingresados
    def confirmar_datos(self):
        resultados = []
        for etiqueta, input_field in self.datos_persona:
            valor = input_field.currentText() if isinstance(input_field, QComboBox) else input_field.text()
            if valor:
                resultados.append(f"{etiqueta}: {valor}")
            else:
                resultados.append(f"{etiqueta}: Faltan datos")

        # Mostrar los resultados en la etiqueta
        self.resultado_label.setText("\n".join(resultados))

# Crear la aplicación
app = QApplication(sys.argv)
# Crear la ventana principal
ventana = MainVentana()
# Mostrar la ventana
ventana.show()
# Ejecutar la aplicación
sys.exit(app.exec_())

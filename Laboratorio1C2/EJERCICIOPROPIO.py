'''Este es un programa que nos permite organizar la información académica de un estudiante de forma rápida y sin complicaciones, 
haciendo que el proceso sea menos tedioso y más eficiente.'''

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QRadioButton, QComboBox, QSpinBox, QPushButton
)

class MainVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 400, 350)
        self.setWindowTitle("Información de Estudiantes")

        # Crear un widget central
        central = QWidget(self)
        self.setCentralWidget(central)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Crear radio buttons para seleccionar el tipo de estudio
        self.tipo_estudio_label = QLabel("Selecciona tu tipo de estudio:")
        self.tipo_radio1 = QRadioButton("Técnico")
        self.tipo_radio2 = QRadioButton("Ingeniería")
        self.tipo_radio3 = QRadioButton("Licenciatura")
        self.tipo_radio4 = QRadioButton("Profesorado")
        self.tipo_radio5 = QRadioButton("Medicina")

        # Añadir los radio buttons al layout
        layout.addWidget(self.tipo_estudio_label)
        layout.addWidget(self.tipo_radio1)
        layout.addWidget(self.tipo_radio2)
        layout.addWidget(self.tipo_radio3)
        layout.addWidget(self.tipo_radio4)
        layout.addWidget(self.tipo_radio5)

        # Crear un combo box para seleccionar la carrera
        self.carrera_label = QLabel("Selecciona tu carrera:")
        self.carrera_combo = QComboBox()
        self.carrera_combo.addItems([
            "Ingeniería Civil", "Ingeniería de Software", "Medicina General", "Psicología", 
            "Administración de Empresas", "Profesorado de Matemáticas", "Arquitectura", 
            "Diseño Gráfico", "Técnico en Electrónica", "Técnico en Mecánica"
        ])

        # Añadir el combo box al layout
        layout.addWidget(self.carrera_label)
        layout.addWidget(self.carrera_combo)

        # Crear un combo box para seleccionar el ciclo
        self.ciclo_label = QLabel("Selecciona el ciclo que estás cursando:")
        self.ciclo_combo = QComboBox()
        self.ciclo_combo.addItems(["1°", "2°", "3°", "4°", "5°", "6°", "7°", "8°", "9°", "10°"])

        # Añadir el combo box del ciclo al layout
        layout.addWidget(self.ciclo_label)
        layout.addWidget(self.ciclo_combo)

        # Crear un spin box para seleccionar el número de créditos
        self.creditos_label = QLabel("Selecciona la cantidad de créditos:")
        self.creditos_spin = QSpinBox()
        self.creditos_spin.setMinimum(1)
        self.creditos_spin.setMaximum(50)

        # Añadir el spin box al layout
        layout.addWidget(self.creditos_label)
        layout.addWidget(self.creditos_spin)

        # Botón para confirmar la selección
        self.confirmar_datos_btn = QPushButton("Confirmar")
        self.confirmar_datos_btn.clicked.connect(self.confirmar_datos)

        # Etiqueta para mostrar el resultado
        self.resultado_label = QLabel("")

        # Añadir el botón y la etiqueta al layout
        layout.addWidget(self.confirmar_datos_btn)
        layout.addWidget(self.resultado_label)

        # Asignar el layout al widget central
        central.setLayout(layout)

    # Función para confirmar la selección
    def confirmar_datos(self):
        tipo_estudio = ""
        if self.tipo_radio1.isChecked():
            tipo_estudio = "Técnico"
        elif self.tipo_radio2.isChecked():
            tipo_estudio = "Ingeniería"
        elif self.tipo_radio3.isChecked():
            tipo_estudio = "Licenciatura"
        elif self.tipo_radio4.isChecked():
            tipo_estudio = "Profesorado"
        elif self.tipo_radio5.isChecked():
            tipo_estudio = "Medicina"
        
        carrera = self.carrera_combo.currentText()
        ciclo = self.ciclo_combo.currentText()
        creditos = self.creditos_spin.value()

        if tipo_estudio and carrera and ciclo:
            resultado = f"Tipo de estudio: {tipo_estudio}\nCarrera: {carrera}\nCiclo: {ciclo}\nCréditos: {creditos}"
        else:
            resultado = "Por favor, selecciona todos los campos."

        self.resultado_label.setText(resultado)


app = QApplication(sys.argv)
ventana = MainVentana()
ventana.show()
app.exec()


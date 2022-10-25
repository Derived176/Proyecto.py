# Importar bibliotecas
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton


# Subclase QMainWindow
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(740, 520)
        self.setWindowTitle("MEMEFLIX")
        contenedor = QWidget()
        self.setStyleSheet("background-color: #0000.")
        lyt_principal = QGridLayout()

        self.lnedtTexto = QLineEdit()
        btn_busca = QPushButton("Buscar")

        lyt_principal.addWidget(self.lnedtTexto, 0, 0)
        lyt_principal.addWidget(btn_busca, 0, 1)

        contenedor.setLayout(lyt_principal)
        self.setMenuWidget(contenedor)

app = QApplication([])
window = Main()
window.show()

app.exec_()

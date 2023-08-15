
import sys
from PySide2 import QtWidgets, QtCore


class InterfaceViaCodigo(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.input = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('OK')
        self.label = QtWidgets.QLabel('Nome')

        self.__config_layout()

    def __config_layout(self):
        self.input.setPlaceholderText('Digite seu nome')
        self.button.clicked.connect(self.__button_clicked)
        self.label.setAlignment(QtCore.Qt.AlignTop)

        # self.input.setParent(self.main_layout)
        # self.button.setParent(self.main_layout)
        # self.label.setParent(self.main_layout)

        self.main_layout.addWidget(self.input)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.label)

    def __button_clicked(self):
        text = self.input.text().upper()
        self.label.setText(f'Nome digitado é: {text}')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    my_widget = InterfaceViaCodigo()
    my_widget.resize(500, 200)
    my_widget.show()

    sys.exit(app.exec_())

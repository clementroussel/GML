from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QSpinBox, QHBoxLayout, QPushButton, QFileDialog, QGroupBox
from PyQt5.QtCore import Qt

import os
import numpy as np
import wget


class MainWindow(QMainWindow):
    def __init__(self, appctxt):
        super().__init__()

        self.success = []
        self.fails = []
        
        self.setWindowTitle("Get My LiDAR !")

        centralWidget = QWidget()
        mainLayout = QVBoxLayout()

        group = QGroupBox("URL parameters")
        layout = QGridLayout()

        label = QLabel("main url :")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 0, 0)
        
        self.main_url = QLineEdit()
        self.main_url.setText("https://wxs.ign.fr")
        self.main_url.textEdited.connect(self.update_first_url)
        layout.addWidget(self.main_url, 0, 1)

        label = QLabel("token :")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 1, 0)
        
        self.token = QLineEdit()
        self.token.setText("c90xknypoz1flvgojchbphgt")
        self.token.textEdited.connect(self.update_first_url)
        layout.addWidget(self.token, 1, 1)

        label = QLabel("id :")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 2, 0)
        
        self.id = QLineEdit()
        self.id.textEdited.connect(self.update_first_url)
        layout.addWidget(self.id, 2, 1)

        label = QLabel("year :")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 3, 0)
        
        self.year = QSpinBox()
        self.year.setRange(2020, 2050)
        self.year.setValue(2021)
        self.year.valueChanged.connect(self.update_first_url)
        layout.addWidget(self.year, 3, 1)

        label = QLabel("x start :")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 4, 0)
        
        self.x_start = QSpinBox()
        self.x_start.setRange(0, 9999)
        self.x_start.valueChanged.connect(self.update_first_url)
        layout.addWidget(self.x_start, 4, 1)

        label = QLabel("x end :")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 5, 0)
        
        self.x_end = QSpinBox()
        self.x_end.setRange(0, 9999)
        self.x_end.valueChanged.connect(self.update_first_url)
        layout.addWidget(self.x_end, 5, 1)

        label = QLabel("y start :")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 6, 0)
        
        self.y_start = QSpinBox()
        self.y_start.setRange(0, 9999)
        self.y_start.valueChanged.connect(self.update_first_url)
        layout.addWidget(self.y_start, 6, 1)

        label = QLabel("y end :")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(label, 7, 0)
        
        self.y_end = QSpinBox()
        self.y_end.setRange(0, 9999)
        self.y_end.valueChanged.connect(self.update_first_url)
        layout.addWidget(self.y_end, 7, 1)

        group.setLayout(layout)
        mainLayout.addWidget(group)

        group = QGroupBox("First URL")
        layout = QVBoxLayout()

        self.first_url = QLabel()
        self.first_url.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        url = f"{self.main_url.text()}/{self.token.text()}/telechargement/prepackage/LIDARHD_PACK_{self.id.text()}_{self.year.value()}$LIDARHD_1-0_LAZ_{self.id.text()}-{str(self.x_start.value()).zfill(4)}_{str(self.y_start.value()).zfill(4)}-{self.year.value()}/file/LIDARHD_1-0_LAZ_{self.id.text()}-{str(self.x_start.value()).zfill(4)}_{str(self.y_start.value()).zfill(4)}-{self.year.value()}.7z"
        self.first_url.setText(url)
        layout.addWidget(self.first_url)

        group.setLayout(layout)
        mainLayout.addWidget(group)

        group = QGroupBox("Destination folder")
        layout = QHBoxLayout()

        self.path = QLineEdit()
        self.path.setText(os.getcwd())
        self.path.setReadOnly(True)
        layout.addWidget(self.path)

        browse = QPushButton("...")
        browse.clicked.connect(self.browse)
        layout.addWidget(browse)

        group.setLayout(layout)
        mainLayout.addWidget(group)

        layout = QHBoxLayout()

        gml = QPushButton("Get My LiDAR !")
        gml.clicked.connect(self.get_my_lidar)
        layout.addWidget(gml)

        again = QPushButton("Try again !")
        again.clicked.connect(self.try_again)
        layout.addWidget(again)

        mainLayout.addLayout(layout)

        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def update_first_url(self):
        url = f"{self.main_url.text()}/{self.token.text()}/telechargement/prepackage/LIDARHD_PACK_{self.id.text()}_{self.year.value()}$LIDARHD_1-0_LAZ_{self.id.text()}-{str(self.x_start.value()).zfill(4)}_{str(self.y_start.value()).zfill(4)}-{self.year.value()}/file/LIDARHD_1-0_LAZ_{self.id.text()}-{str(self.x_start.value()).zfill(4)}_{str(self.y_start.value()).zfill(4)}-{self.year.value()}.7z"
        self.first_url.setText(url)

    def get_my_lidar(self):
        os.chdir(self.path.text())

        east = np.arange(self.x_start.value(), self.x_end.value() + 2, 2)
        north = np.arange(self.y_start.value(), self.y_end.value() + 2, 2)

        for e in east:
            for n in north:
                # url configuration
                url = f"{self.main_url.text()}/{self.token.text()}/telechargement/prepackage/LIDARHD_PACK_{self.id.text()}_{self.year.value()}$LIDARHD_1-0_LAZ_{self.id.text()}-{str(e).zfill(4)}_{str(n).zfill(4)}-{self.year.value()}/file/LIDARHD_1-0_LAZ_{self.id.text()}-{str(e).zfill(4)}_{str(n).zfill(4)}-{self.year.value()}.7z"

                # downloading
                print("Downloading file: {}".format(url.split("/")[-1]))
                try:
                    wget.download(url)
                except:
                    self.fails.append(url)
                    print("Empty url. Next !")
                    print("----")
                    continue
                else:
                    self.success.append(url)
                    print("\nDone !")
                    print("----")
                
        print(f"{len(self.success)} file(s) downloaded.")
        print(f"{len(self.fails)} empty url(s).")
        print("\n")

    def browse(self):
        path = QFileDialog.getExistingDirectory(self, 'Select destination folder')
        if path != "":
            self.path.setText(path)

    def try_again(self):
        fails = []
        for url in self.fails:
            print("Downloading file: {}".format(url.split("/")[-1]))
            try:
                wget.download(url)
            except:
                fails.append(url)
                print("Empty url. Next !")
                print("----")
                continue
            else:
                self.success.append(url)
                print("\nDone !")
                print("----")
                
        self.fails = fails
        print(f"{len(self.success)} file(s) downloaded.")
        print(f"{len(self.fails)} empty url(s).")
        print("\n")
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyecto1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source5

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(649, 651)
        self.actionAgregar_productos = QAction(MainWindow)
        self.actionAgregar_productos.setObjectName(u"actionAgregar_productos")
        self.actionVer_inventario = QAction(MainWindow)
        self.actionVer_inventario.setObjectName(u"actionVer_inventario")
        self.actionModificar_datos = QAction(MainWindow)
        self.actionModificar_datos.setObjectName(u"actionModificar_datos")
        self.actionBuscar_productos = QAction(MainWindow)
        self.actionBuscar_productos.setObjectName(u"actionBuscar_productos")
        self.actionEliminar_productos = QAction(MainWindow)
        self.actionEliminar_productos.setObjectName(u"actionEliminar_productos")
        self.actionAgregar_pedidos = QAction(MainWindow)
        self.actionAgregar_pedidos.setObjectName(u"actionAgregar_pedidos")
        self.actionVer_pedidos = QAction(MainWindow)
        self.actionVer_pedidos.setObjectName(u"actionVer_pedidos")
        self.actionModificar_pedidos = QAction(MainWindow)
        self.actionModificar_pedidos.setObjectName(u"actionModificar_pedidos")
        self.actionBuscar_pedidos = QAction(MainWindow)
        self.actionBuscar_pedidos.setObjectName(u"actionBuscar_pedidos")
        self.actionEliminar_pedidos = QAction(MainWindow)
        self.actionEliminar_pedidos.setObjectName(u"actionEliminar_pedidos")
        self.actionAgregar_ventas = QAction(MainWindow)
        self.actionAgregar_ventas.setObjectName(u"actionAgregar_ventas")
        self.actionVer_ventas = QAction(MainWindow)
        self.actionVer_ventas.setObjectName(u"actionVer_ventas")
        self.actionBuscar_ventas = QAction(MainWindow)
        self.actionBuscar_ventas.setObjectName(u"actionBuscar_ventas")
        self.actionCalcular_total = QAction(MainWindow)
        self.actionCalcular_total.setObjectName(u"actionCalcular_total")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_21 = QGridLayout(self.centralwidget)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"\n"
"QWidget\n"
"{background-image: url(:/images/images/madera.png);\n"
"}\n"
"\n"
"QLabel#tabacos{\n"
"color:black;\n"
"font-size:50px;\n"
"font-family: courier new;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#ornelas{\n"
"color:black;\n"
"font-size:50px;\n"
"font-family: courier new;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro2{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro3{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro4{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro5{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro6{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro7{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro8{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro9{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#puro10{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QLabel#bienvenido{\n"
"background"
                        ":none;\n"
"font-size:15px;\n"
"}\n"
"\n"
"QGroupBox#puros{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"\n"
"QGroupBox#puros2{\n"
"border:none;\n"
"background:none;\n"
"}")
        self.gridLayout_16 = QGridLayout(self.tab)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.puros = QGroupBox(self.tab)
        self.puros.setObjectName(u"puros")
        self.horizontalLayout = QHBoxLayout(self.puros)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.puro5 = QLabel(self.puros)
        self.puro5.setObjectName(u"puro5")
        self.puro5.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.horizontalLayout.addWidget(self.puro5)

        self.puro3 = QLabel(self.puros)
        self.puro3.setObjectName(u"puro3")
        self.puro3.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.horizontalLayout.addWidget(self.puro3)

        self.puro4 = QLabel(self.puros)
        self.puro4.setObjectName(u"puro4")
        self.puro4.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.horizontalLayout.addWidget(self.puro4)

        self.puro = QLabel(self.puros)
        self.puro.setObjectName(u"puro")
        self.puro.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.horizontalLayout.addWidget(self.puro)

        self.puro2 = QLabel(self.puros)
        self.puro2.setObjectName(u"puro2")
        self.puro2.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.horizontalLayout.addWidget(self.puro2)


        self.gridLayout_16.addWidget(self.puros, 0, 0, 1, 1)

        self.bienvenido = QLabel(self.tab)
        self.bienvenido.setObjectName(u"bienvenido")
        self.bienvenido.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.bienvenido, 4, 0, 1, 1)

        self.puros2 = QGroupBox(self.tab)
        self.puros2.setObjectName(u"puros2")
        self.gridLayout_2 = QGridLayout(self.puros2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.puro7 = QLabel(self.puros2)
        self.puro7.setObjectName(u"puro7")
        self.puro7.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.gridLayout_2.addWidget(self.puro7, 0, 0, 1, 1)

        self.puro8 = QLabel(self.puros2)
        self.puro8.setObjectName(u"puro8")
        self.puro8.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.gridLayout_2.addWidget(self.puro8, 0, 1, 1, 1)

        self.puro6 = QLabel(self.puros2)
        self.puro6.setObjectName(u"puro6")
        self.puro6.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.gridLayout_2.addWidget(self.puro6, 0, 2, 1, 1)

        self.puro9 = QLabel(self.puros2)
        self.puro9.setObjectName(u"puro9")
        self.puro9.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.gridLayout_2.addWidget(self.puro9, 0, 3, 1, 1)

        self.puro10 = QLabel(self.puros2)
        self.puro10.setObjectName(u"puro10")
        self.puro10.setStyleSheet(u"image: url(:/prefijoNuevo/images/puro.png);")

        self.gridLayout_2.addWidget(self.puro10, 0, 4, 1, 1)


        self.gridLayout_16.addWidget(self.puros2, 3, 0, 1, 1)

        self.ornelas = QLabel(self.tab)
        self.ornelas.setObjectName(u"ornelas")
        self.ornelas.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.ornelas, 2, 0, 1, 1)

        self.tabacos = QLabel(self.tab)
        self.tabacos.setObjectName(u"tabacos")
        self.tabacos.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.tabacos, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_18 = QGridLayout(self.tab_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox = QGroupBox(self.groupBox_7)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_buscar_modificar_inventario = QPushButton(self.groupBox)
        self.pushButton_buscar_modificar_inventario.setObjectName(u"pushButton_buscar_modificar_inventario")

        self.gridLayout.addWidget(self.pushButton_buscar_modificar_inventario, 2, 0, 1, 2)

        self.lineEdit_cantidad_modificar_inventario = QLineEdit(self.groupBox)
        self.lineEdit_cantidad_modificar_inventario.setObjectName(u"lineEdit_cantidad_modificar_inventario")
        self.lineEdit_cantidad_modificar_inventario.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cantidad_modificar_inventario, 4, 0, 1, 1)

        self.lineEdit_precio_modificar_inventario = QLineEdit(self.groupBox)
        self.lineEdit_precio_modificar_inventario.setObjectName(u"lineEdit_precio_modificar_inventario")
        self.lineEdit_precio_modificar_inventario.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_precio_modificar_inventario, 4, 1, 1, 1)

        self.pushButton_modificar_inventario = QPushButton(self.groupBox)
        self.pushButton_modificar_inventario.setObjectName(u"pushButton_modificar_inventario")

        self.gridLayout.addWidget(self.pushButton_modificar_inventario, 5, 0, 1, 2)

        self.lineEdit_agregar_modificar_inventario = QLineEdit(self.groupBox)
        self.lineEdit_agregar_modificar_inventario.setObjectName(u"lineEdit_agregar_modificar_inventario")
        self.lineEdit_agregar_modificar_inventario.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_agregar_modificar_inventario, 3, 0, 1, 2)

        self.lineEdit_buscar_modificar_inventario = QLineEdit(self.groupBox)
        self.lineEdit_buscar_modificar_inventario.setObjectName(u"lineEdit_buscar_modificar_inventario")
        self.lineEdit_buscar_modificar_inventario.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_buscar_modificar_inventario, 1, 0, 1, 2)


        self.gridLayout_9.addWidget(self.groupBox, 5, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox_7)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_13 = QGridLayout(self.groupBox_10)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lineEdit_buscar_inventario = QLineEdit(self.groupBox_10)
        self.lineEdit_buscar_inventario.setObjectName(u"lineEdit_buscar_inventario")
        self.lineEdit_buscar_inventario.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.lineEdit_buscar_inventario, 0, 0, 1, 2)

        self.pushButton_eliminar_inventario = QPushButton(self.groupBox_10)
        self.pushButton_eliminar_inventario.setObjectName(u"pushButton_eliminar_inventario")

        self.gridLayout_13.addWidget(self.pushButton_eliminar_inventario, 1, 1, 1, 1)

        self.pushButton_buscar_inventario = QPushButton(self.groupBox_10)
        self.pushButton_buscar_inventario.setObjectName(u"pushButton_buscar_inventario")

        self.gridLayout_13.addWidget(self.pushButton_buscar_inventario, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_10, 4, 0, 1, 2)

        self.pushButton_ver_inventario = QPushButton(self.groupBox_7)
        self.pushButton_ver_inventario.setObjectName(u"pushButton_ver_inventario")

        self.gridLayout_9.addWidget(self.pushButton_ver_inventario, 3, 0, 1, 2)

        self.groupBox_9 = QGroupBox(self.groupBox_7)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_12 = QGridLayout(self.groupBox_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lineEdit_cantidad_inventario = QLineEdit(self.groupBox_9)
        self.lineEdit_cantidad_inventario.setObjectName(u"lineEdit_cantidad_inventario")
        self.lineEdit_cantidad_inventario.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.lineEdit_cantidad_inventario, 2, 0, 1, 1)

        self.lineEdit_agregar_inventario = QLineEdit(self.groupBox_9)
        self.lineEdit_agregar_inventario.setObjectName(u"lineEdit_agregar_inventario")
        self.lineEdit_agregar_inventario.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.lineEdit_agregar_inventario, 1, 0, 1, 2)

        self.lineEdit_precio_inventario = QLineEdit(self.groupBox_9)
        self.lineEdit_precio_inventario.setObjectName(u"lineEdit_precio_inventario")
        self.lineEdit_precio_inventario.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.lineEdit_precio_inventario, 2, 1, 1, 1)

        self.pushButton_agregar_inventario = QPushButton(self.groupBox_9)
        self.pushButton_agregar_inventario.setObjectName(u"pushButton_agregar_inventario")

        self.gridLayout_12.addWidget(self.pushButton_agregar_inventario, 3, 0, 1, 2)


        self.gridLayout_9.addWidget(self.groupBox_9, 6, 0, 1, 1)

        self.tableWidget_inventario = QTableWidget(self.groupBox_7)
        self.tableWidget_inventario.setObjectName(u"tableWidget_inventario")
        self.tableWidget_inventario.setLineWidth(1)
        self.tableWidget_inventario.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_inventario.setAlternatingRowColors(True)
        self.tableWidget_inventario.horizontalHeader().setDefaultSectionSize(140)

        self.gridLayout_9.addWidget(self.tableWidget_inventario, 0, 0, 2, 2)


        self.gridLayout_18.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_8 = QGroupBox(self.tab_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_11 = QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableWidget_pedidos = QTableWidget(self.groupBox_8)
        self.tableWidget_pedidos.setObjectName(u"tableWidget_pedidos")
        self.tableWidget_pedidos.setAlternatingRowColors(True)
        self.tableWidget_pedidos.horizontalHeader().setDefaultSectionSize(170)

        self.gridLayout_11.addWidget(self.tableWidget_pedidos, 0, 0, 1, 2)

        self.groupBox_11 = QGroupBox(self.groupBox_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_14 = QGridLayout(self.groupBox_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.lineEdit_ver_pedidos = QLineEdit(self.groupBox_11)
        self.lineEdit_ver_pedidos.setObjectName(u"lineEdit_ver_pedidos")
        self.lineEdit_ver_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.lineEdit_ver_pedidos, 0, 0, 1, 1)

        self.pushButton_ver_pedidos = QPushButton(self.groupBox_11)
        self.pushButton_ver_pedidos.setObjectName(u"pushButton_ver_pedidos")

        self.gridLayout_14.addWidget(self.pushButton_ver_pedidos, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_11, 1, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBox_8)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_4 = QGridLayout(self.groupBox_13)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_eliminar_pedidos = QPushButton(self.groupBox_13)
        self.pushButton_eliminar_pedidos.setObjectName(u"pushButton_eliminar_pedidos")

        self.gridLayout_4.addWidget(self.pushButton_eliminar_pedidos, 3, 1, 1, 1)

        self.lineEdit_buscar_pedidos = QLineEdit(self.groupBox_13)
        self.lineEdit_buscar_pedidos.setObjectName(u"lineEdit_buscar_pedidos")
        self.lineEdit_buscar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_buscar_pedidos, 1, 0, 1, 2)

        self.pushButton_buscar_pedidos = QPushButton(self.groupBox_13)
        self.pushButton_buscar_pedidos.setObjectName(u"pushButton_buscar_pedidos")

        self.gridLayout_4.addWidget(self.pushButton_buscar_pedidos, 3, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_13, 1, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.groupBox_8)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_17 = QGridLayout(self.groupBox_14)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.lineEdit_fecha_modificar_pedidos = QLineEdit(self.groupBox_14)
        self.lineEdit_fecha_modificar_pedidos.setObjectName(u"lineEdit_fecha_modificar_pedidos")
        self.lineEdit_fecha_modificar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lineEdit_fecha_modificar_pedidos, 4, 0, 1, 1)

        self.lineEdit_nombre_cliente_modificar_pedidos = QLineEdit(self.groupBox_14)
        self.lineEdit_nombre_cliente_modificar_pedidos.setObjectName(u"lineEdit_nombre_cliente_modificar_pedidos")
        self.lineEdit_nombre_cliente_modificar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lineEdit_nombre_cliente_modificar_pedidos, 5, 0, 1, 1)

        self.lineEdit_fecha_entrega_modificar_pedidos = QLineEdit(self.groupBox_14)
        self.lineEdit_fecha_entrega_modificar_pedidos.setObjectName(u"lineEdit_fecha_entrega_modificar_pedidos")
        self.lineEdit_fecha_entrega_modificar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lineEdit_fecha_entrega_modificar_pedidos, 4, 1, 1, 1)

        self.lineEdit_telefono_cliente_modificar_pedidos = QLineEdit(self.groupBox_14)
        self.lineEdit_telefono_cliente_modificar_pedidos.setObjectName(u"lineEdit_telefono_cliente_modificar_pedidos")
        self.lineEdit_telefono_cliente_modificar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lineEdit_telefono_cliente_modificar_pedidos, 5, 1, 1, 1)

        self.pushButton_buscar_modificar_pedidos = QPushButton(self.groupBox_14)
        self.pushButton_buscar_modificar_pedidos.setObjectName(u"pushButton_buscar_modificar_pedidos")

        self.gridLayout_17.addWidget(self.pushButton_buscar_modificar_pedidos, 1, 0, 1, 2)

        self.pushButton_modificar_pedidos = QPushButton(self.groupBox_14)
        self.pushButton_modificar_pedidos.setObjectName(u"pushButton_modificar_pedidos")

        self.gridLayout_17.addWidget(self.pushButton_modificar_pedidos, 6, 0, 1, 2)

        self.lineEdit_cantidad_modificar_pedidos = QLineEdit(self.groupBox_14)
        self.lineEdit_cantidad_modificar_pedidos.setObjectName(u"lineEdit_cantidad_modificar_pedidos")
        self.lineEdit_cantidad_modificar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lineEdit_cantidad_modificar_pedidos, 3, 1, 1, 1)

        self.lineEdit_agregar_modificar_pedidos = QLineEdit(self.groupBox_14)
        self.lineEdit_agregar_modificar_pedidos.setObjectName(u"lineEdit_agregar_modificar_pedidos")
        self.lineEdit_agregar_modificar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lineEdit_agregar_modificar_pedidos, 3, 0, 1, 1)

        self.lineEdit_buscar_modificar_pedidos = QLineEdit(self.groupBox_14)
        self.lineEdit_buscar_modificar_pedidos.setObjectName(u"lineEdit_buscar_modificar_pedidos")
        self.lineEdit_buscar_modificar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lineEdit_buscar_modificar_pedidos, 0, 0, 1, 2)


        self.gridLayout_11.addWidget(self.groupBox_14, 2, 0, 1, 2)

        self.groupBox_12 = QGroupBox(self.groupBox_8)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_15 = QGridLayout(self.groupBox_12)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.lineEdit_fecha_entrega_pedidos = QLineEdit(self.groupBox_12)
        self.lineEdit_fecha_entrega_pedidos.setObjectName(u"lineEdit_fecha_entrega_pedidos")
        self.lineEdit_fecha_entrega_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lineEdit_fecha_entrega_pedidos, 2, 1, 1, 1)

        self.pushButton_agregar_pedidos = QPushButton(self.groupBox_12)
        self.pushButton_agregar_pedidos.setObjectName(u"pushButton_agregar_pedidos")

        self.gridLayout_15.addWidget(self.pushButton_agregar_pedidos, 4, 0, 1, 2)

        self.lineEdit_nombre_cliente_pedidos = QLineEdit(self.groupBox_12)
        self.lineEdit_nombre_cliente_pedidos.setObjectName(u"lineEdit_nombre_cliente_pedidos")
        self.lineEdit_nombre_cliente_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lineEdit_nombre_cliente_pedidos, 3, 0, 1, 1)

        self.lineEdit_fecha_pedidos = QLineEdit(self.groupBox_12)
        self.lineEdit_fecha_pedidos.setObjectName(u"lineEdit_fecha_pedidos")
        self.lineEdit_fecha_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lineEdit_fecha_pedidos, 2, 0, 1, 1)

        self.lineEdit_telefono_cliente_pedidos = QLineEdit(self.groupBox_12)
        self.lineEdit_telefono_cliente_pedidos.setObjectName(u"lineEdit_telefono_cliente_pedidos")
        self.lineEdit_telefono_cliente_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lineEdit_telefono_cliente_pedidos, 3, 1, 1, 1)

        self.lineEdit_agregar_pedidos = QLineEdit(self.groupBox_12)
        self.lineEdit_agregar_pedidos.setObjectName(u"lineEdit_agregar_pedidos")
        self.lineEdit_agregar_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lineEdit_agregar_pedidos, 1, 0, 1, 1)

        self.lineEdit_cantidad_pedidos = QLineEdit(self.groupBox_12)
        self.lineEdit_cantidad_pedidos.setObjectName(u"lineEdit_cantidad_pedidos")
        self.lineEdit_cantidad_pedidos.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lineEdit_cantidad_pedidos, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_12, 3, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_8 = QGridLayout(self.tab_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_3 = QGroupBox(self.tab_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lineEdit_ver_ventas = QLineEdit(self.groupBox_4)
        self.lineEdit_ver_ventas.setObjectName(u"lineEdit_ver_ventas")
        self.lineEdit_ver_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_ver_ventas, 0, 0, 1, 1)

        self.pushButton_ver_total_ventas = QPushButton(self.groupBox_4)
        self.pushButton_ver_total_ventas.setObjectName(u"pushButton_ver_total_ventas")

        self.gridLayout_10.addWidget(self.pushButton_ver_total_ventas, 2, 0, 1, 1)

        self.pushButton_ver_ventas = QPushButton(self.groupBox_4)
        self.pushButton_ver_ventas.setObjectName(u"pushButton_ver_ventas")

        self.gridLayout_10.addWidget(self.pushButton_ver_ventas, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_eliminar_ventas = QPushButton(self.groupBox_5)
        self.pushButton_eliminar_ventas.setObjectName(u"pushButton_eliminar_ventas")

        self.gridLayout_3.addWidget(self.pushButton_eliminar_ventas, 1, 3, 1, 1)

        self.pushButton_buscar_ventas = QPushButton(self.groupBox_5)
        self.pushButton_buscar_ventas.setObjectName(u"pushButton_buscar_ventas")

        self.gridLayout_3.addWidget(self.pushButton_buscar_ventas, 1, 1, 1, 2)

        self.lineEdit_buscar_ventas = QLineEdit(self.groupBox_5)
        self.lineEdit_buscar_ventas.setObjectName(u"lineEdit_buscar_ventas")
        self.lineEdit_buscar_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_buscar_ventas, 0, 1, 1, 3)


        self.gridLayout_7.addWidget(self.groupBox_5, 1, 2, 1, 1)

        self.tableWidget_ventas = QTableWidget(self.groupBox_3)
        self.tableWidget_ventas.setObjectName(u"tableWidget_ventas")
        self.tableWidget_ventas.setAlternatingRowColors(True)
        self.tableWidget_ventas.horizontalHeader().setDefaultSectionSize(150)

        self.gridLayout_7.addWidget(self.tableWidget_ventas, 0, 0, 1, 3)

        self.groupBox_15 = QGroupBox(self.groupBox_3)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_20 = QGridLayout(self.groupBox_15)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.lineEdit_fecha_modificar_ventas = QLineEdit(self.groupBox_15)
        self.lineEdit_fecha_modificar_ventas.setObjectName(u"lineEdit_fecha_modificar_ventas")
        self.lineEdit_fecha_modificar_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.lineEdit_fecha_modificar_ventas, 3, 1, 1, 1)

        self.lineEdit_cantidad_modificar_ventas = QLineEdit(self.groupBox_15)
        self.lineEdit_cantidad_modificar_ventas.setObjectName(u"lineEdit_cantidad_modificar_ventas")
        self.lineEdit_cantidad_modificar_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.lineEdit_cantidad_modificar_ventas, 3, 0, 1, 1)

        self.lineEdit_agregar_modificar_ventas = QLineEdit(self.groupBox_15)
        self.lineEdit_agregar_modificar_ventas.setObjectName(u"lineEdit_agregar_modificar_ventas")
        self.lineEdit_agregar_modificar_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.lineEdit_agregar_modificar_ventas, 2, 0, 1, 2)

        self.pushButton_modificar_ventas = QPushButton(self.groupBox_15)
        self.pushButton_modificar_ventas.setObjectName(u"pushButton_modificar_ventas")

        self.gridLayout_20.addWidget(self.pushButton_modificar_ventas, 4, 0, 1, 2)

        self.pushButton_buscar_modificar_ventas = QPushButton(self.groupBox_15)
        self.pushButton_buscar_modificar_ventas.setObjectName(u"pushButton_buscar_modificar_ventas")

        self.gridLayout_20.addWidget(self.pushButton_buscar_modificar_ventas, 1, 0, 1, 2)

        self.lineEdit_buscar_modificar_ventas = QLineEdit(self.groupBox_15)
        self.lineEdit_buscar_modificar_ventas.setObjectName(u"lineEdit_buscar_modificar_ventas")
        self.lineEdit_buscar_modificar_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.lineEdit_buscar_modificar_ventas, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.groupBox_15, 4, 0, 1, 3)

        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_cantidad_ventas = QLineEdit(self.groupBox_6)
        self.lineEdit_cantidad_ventas.setObjectName(u"lineEdit_cantidad_ventas")
        self.lineEdit_cantidad_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_cantidad_ventas, 2, 0, 1, 1)

        self.lineEdit_agregar_ventas = QLineEdit(self.groupBox_6)
        self.lineEdit_agregar_ventas.setObjectName(u"lineEdit_agregar_ventas")
        self.lineEdit_agregar_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_agregar_ventas, 1, 0, 1, 2)

        self.lineEdit_fecha_ventas = QLineEdit(self.groupBox_6)
        self.lineEdit_fecha_ventas.setObjectName(u"lineEdit_fecha_ventas")
        self.lineEdit_fecha_ventas.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_fecha_ventas, 2, 1, 1, 1)

        self.pushButton_agregar_ventas = QPushButton(self.groupBox_6)
        self.pushButton_agregar_ventas.setObjectName(u"pushButton_agregar_ventas")

        self.gridLayout_6.addWidget(self.pushButton_agregar_ventas, 3, 0, 1, 2)


        self.gridLayout_7.addWidget(self.groupBox_6, 5, 0, 1, 3)


        self.gridLayout_8.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_21.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 649, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAgregar_productos.setText(QCoreApplication.translate("MainWindow", u"Agregar productos", None))
        self.actionVer_inventario.setText(QCoreApplication.translate("MainWindow", u"Ver inventario", None))
        self.actionModificar_datos.setText(QCoreApplication.translate("MainWindow", u"Modificar datos", None))
        self.actionBuscar_productos.setText(QCoreApplication.translate("MainWindow", u"Buscar productos", None))
        self.actionEliminar_productos.setText(QCoreApplication.translate("MainWindow", u"Eliminar productos", None))
        self.actionAgregar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Agregar pedidos", None))
        self.actionVer_pedidos.setText(QCoreApplication.translate("MainWindow", u"Ver pedidos", None))
        self.actionModificar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Modificar pedidos", None))
        self.actionBuscar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Buscar pedidos", None))
        self.actionEliminar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Eliminar pedidos", None))
        self.actionAgregar_ventas.setText(QCoreApplication.translate("MainWindow", u"Agregar ventas", None))
        self.actionVer_ventas.setText(QCoreApplication.translate("MainWindow", u"Ver ventas", None))
        self.actionBuscar_ventas.setText(QCoreApplication.translate("MainWindow", u"Buscar ventas", None))
        self.actionCalcular_total.setText(QCoreApplication.translate("MainWindow", u"Calcular total", None))
        self.puros.setTitle("")
        self.puro5.setText("")
        self.puro3.setText("")
        self.puro4.setText("")
        self.puro.setText("")
        self.puro2.setText("")
        self.bienvenido.setText(QCoreApplication.translate("MainWindow", u"Bienvenido, Administrador", None))
        self.puros2.setTitle("")
        self.puro7.setText("")
        self.puro8.setText("")
        self.puro6.setText("")
        self.puro9.setText("")
        self.puro10.setText("")
        self.ornelas.setText(QCoreApplication.translate("MainWindow", u"Ornelas", None))
        self.tabacos.setText(QCoreApplication.translate("MainWindow", u"Tabacos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.groupBox_7.setTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Buscar y Modificar", None))
        self.pushButton_buscar_modificar_inventario.setText(QCoreApplication.translate("MainWindow", u"Buscar producto", None))
        self.lineEdit_cantidad_modificar_inventario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cantidad del producto a modificar", None))
        self.lineEdit_precio_modificar_inventario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio del producto a modificar", None))
        self.pushButton_modificar_inventario.setText(QCoreApplication.translate("MainWindow", u"Modificar producto", None))
        self.lineEdit_agregar_modificar_inventario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del producto a modificar", None))
        self.lineEdit_buscar_modificar_inventario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del producto a buscar", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Buscar y Eliminar", None))
        self.lineEdit_buscar_inventario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del producto a buscar", None))
        self.pushButton_eliminar_inventario.setText(QCoreApplication.translate("MainWindow", u"Eliminar producto", None))
        self.pushButton_buscar_inventario.setText(QCoreApplication.translate("MainWindow", u"Buscar producto", None))
        self.pushButton_ver_inventario.setText(QCoreApplication.translate("MainWindow", u"Ver inventario", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.lineEdit_cantidad_inventario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cantidad disponible del producto", None))
        self.lineEdit_agregar_inventario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del producto", None))
        self.lineEdit_precio_inventario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio del producto", None))
        self.pushButton_agregar_inventario.setText(QCoreApplication.translate("MainWindow", u"Agregar producto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.groupBox_8.setTitle("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.lineEdit_ver_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha de entrega de los pedidos (dd/mm/aaaa)", None))
        self.pushButton_ver_pedidos.setText(QCoreApplication.translate("MainWindow", u"Ver pedidos", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Buscar y Eliminar", None))
        self.pushButton_eliminar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Eliminar pedido", None))
        self.lineEdit_buscar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero del pedido a buscar", None))
        self.pushButton_buscar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Buscar pedido", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Buscar y Modificar", None))
        self.lineEdit_fecha_modificar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha del pedido a modificar", None))
        self.lineEdit_nombre_cliente_modificar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del cliente a modificar", None))
        self.lineEdit_fecha_entrega_modificar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha de entrega a modificar", None))
        self.lineEdit_telefono_cliente_modificar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono del cliente a modificar", None))
        self.pushButton_buscar_modificar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Buscar pedido", None))
        self.pushButton_modificar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Modificar pedido", None))
        self.lineEdit_cantidad_modificar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cantidad pedida a modificar", None))
        self.lineEdit_agregar_modificar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del producto pedido a modificar", None))
        self.lineEdit_buscar_modificar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero del pedido a buscar", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.lineEdit_fecha_entrega_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha de entrega (dd/mm/aaaa)", None))
        self.pushButton_agregar_pedidos.setText(QCoreApplication.translate("MainWindow", u"Agregar pedido", None))
        self.lineEdit_nombre_cliente_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del cliente", None))
        self.lineEdit_fecha_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha del pedido (dd/mm/aaaa)", None))
        self.lineEdit_telefono_cliente_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono del cliente", None))
        self.lineEdit_agregar_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del producto pedido", None))
        self.lineEdit_cantidad_pedidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cantidad pedida", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.groupBox_3.setTitle("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.lineEdit_ver_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha del d\u00eda de las ventas (dd/mm/aaaa)", None))
        self.pushButton_ver_total_ventas.setText(QCoreApplication.translate("MainWindow", u"Ver total", None))
        self.pushButton_ver_ventas.setText(QCoreApplication.translate("MainWindow", u"Ver ventas", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Buscar y Eliminar", None))
        self.pushButton_eliminar_ventas.setText(QCoreApplication.translate("MainWindow", u"Eliminar venta", None))
        self.pushButton_buscar_ventas.setText(QCoreApplication.translate("MainWindow", u"Buscar venta", None))
        self.lineEdit_buscar_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero de la venta a buscar", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Buscar y Modificar", None))
        self.lineEdit_fecha_modificar_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha de la venta a modificar (dd/mm/aaaa)", None))
        self.lineEdit_cantidad_modificar_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cantidad vendida a modificar", None))
        self.lineEdit_agregar_modificar_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Producto de la venta a modificar", None))
        self.pushButton_modificar_ventas.setText(QCoreApplication.translate("MainWindow", u"Modificar venta", None))
        self.pushButton_buscar_modificar_ventas.setText(QCoreApplication.translate("MainWindow", u"Buscar venta", None))
        self.lineEdit_buscar_modificar_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero de la venta a buscar", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.lineEdit_cantidad_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cantidad vendida", None))
        self.lineEdit_agregar_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del producto vendido", None))
        self.lineEdit_fecha_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fecha de la venta (dd/mm/aaaa)", None))
        self.pushButton_agregar_ventas.setText(QCoreApplication.translate("MainWindow", u"Agregar venta", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Ventas", None))
    # retranslateUi


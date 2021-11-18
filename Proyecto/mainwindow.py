from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
import re
import psycopg2

conexion = psycopg2.connect(
    host = 'LocalHost',
    database = 'tabacos_ornelas',
    user = 'postgres',
    password = 'evanilson20'
)

cursor = conexion.cursor()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tabacos Ornelas")
        self.ui.pushButton_ver_inventario.clicked.connect(self.click_ver_inventario)
        self.ui.pushButton_buscar_inventario.clicked.connect(self.click_buscar_inventario)
        self.ui.pushButton_eliminar_inventario.clicked.connect(self.click_eliminar_inventario)
        self.ui.pushButton_agregar_inventario.clicked.connect(self.click_agregar_inventario)
        self.ui.pushButton_modificar_inventario.clicked.connect(self.click_modificar_inventario)
        self.ui.pushButton_buscar_modificar_inventario.clicked.connect(self.click_buscar_modificar_inventario)

        self.ui.pushButton_ver_pedidos.clicked.connect(self.click_ver_pedido)
        self.ui.pushButton_buscar_pedidos.clicked.connect(self.click_buscar_pedido)
        self.ui.pushButton_eliminar_pedidos.clicked.connect(self.click_eliminar_pedido)
        self.ui.pushButton_agregar_pedidos.clicked.connect(self.click_agregar_pedido)
        self.ui.pushButton_modificar_pedidos.clicked.connect(self.click_modificar_pedido)
        self.ui.pushButton_buscar_modificar_pedidos.clicked.connect(self.click_buscar_modificar_pedido)

        self.ui.pushButton_ver_ventas.clicked.connect(self.click_ver_venta)
        self.ui.pushButton_buscar_ventas.clicked.connect(self.click_buscar_venta)
        self.ui.pushButton_eliminar_ventas.clicked.connect(self.click_eliminar_venta)
        self.ui.pushButton_agregar_ventas.clicked.connect(self.click_agregar_venta)
        self.ui.pushButton_ver_total_ventas.clicked.connect(self.click_ver_total_venta)
        self.ui.pushButton_modificar_ventas.clicked.connect(self.click_modificar_venta)
        self.ui.pushButton_buscar_modificar_ventas.clicked.connect(self.click_buscar_modificar_venta)
        
    @Slot()
    def click_ver_inventario(self):
        self.ui.tableWidget_inventario.clear()
        self.ui.tableWidget_inventario.setColumnCount(4)
        headers = ['Nombre del producto', 'Precio', 'Cantidad a pedir', 'Cantidad disponible']
        self.ui.tableWidget_inventario.setHorizontalHeaderLabels(headers)
        cursor.execute('select *from inventario')
        inventario = cursor.fetchall()
        self.ui.tableWidget_inventario.setRowCount(len(inventario))
        row = 0
        for producto in inventario:
            nombre_producto_widget = QTableWidgetItem(str(producto[0]))
            precio_widget = QTableWidgetItem(str(producto[1]))
            cantidad_a_pedir_widget = QTableWidgetItem(str(producto[2]))
            cantidad_disponible_widget = QTableWidgetItem(str(producto[3]))
            self.ui.tableWidget_inventario.setItem(row,0,nombre_producto_widget)
            self.ui.tableWidget_inventario.setItem(row,1,precio_widget)
            self.ui.tableWidget_inventario.setItem(row,2,cantidad_a_pedir_widget)
            self.ui.tableWidget_inventario.setItem(row,3,cantidad_disponible_widget)
            row += 1
    
    @Slot()
    def click_buscar_inventario(self):
        nombreProducto = self.ui.lineEdit_buscar_inventario.text()
        encontrado = False
        cursor.execute("select *from inventario where nombre_producto = '{0}'".format(nombreProducto))
        inventario = cursor.fetchall()
        for producto in inventario:
            if producto[0] == nombreProducto:
                self.ui.tableWidget_inventario.clear()
                self.ui.tableWidget_inventario.setColumnCount(4)
                headers = ['Nombre del producto', 'Precio', 'Cantidad a pedir', 'Cantidad disponible']
                self.ui.tableWidget_inventario.setHorizontalHeaderLabels(headers)
                self.ui.tableWidget_inventario.setRowCount(1)
                nombre_producto_widget = QTableWidgetItem(str(producto[0]))
                precio_widget = QTableWidgetItem(str(producto[1]))
                cantidad_a_pedir_widget = QTableWidgetItem(str(producto[2]))
                cantidad_disponible_widget = QTableWidgetItem(str(producto[3]))
                self.ui.tableWidget_inventario.setItem(0,0,nombre_producto_widget)
                self.ui.tableWidget_inventario.setItem(0,1,precio_widget)
                self.ui.tableWidget_inventario.setItem(0,2,cantidad_a_pedir_widget)
                self.ui.tableWidget_inventario.setItem(0,3,cantidad_disponible_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'El producto no fue encontrado')         
    
    @Slot()
    def click_eliminar_inventario(self):
        nombreProducto = self.ui.lineEdit_buscar_inventario.text()
        encontrado = False
        cursor.execute("select *from inventario where nombre_producto = '{0}'".format(nombreProducto))
        inventario = cursor.fetchall()
        for producto in inventario:
            if producto[0] == nombreProducto:
                encontrado=True
                cursor.execute("delete from inventario where nombre_producto = '{0}'".format(nombreProducto))
                conexion.commit()
                QMessageBox.information( self, "Éxito", "Producto eliminado exitosamente")           
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'El producto no fue encontrado')  
            

    @Slot()
    def click_agregar_inventario(self):
        nombre = self.ui.lineEdit_agregar_inventario.text()
        precio = self.ui.lineEdit_precio_inventario.text()
        cantidad = self.ui.lineEdit_cantidad_inventario.text()
        

        if int(cantidad.isnumeric()) == True and int(precio.isnumeric()) == True:
            precio = int(precio)
            cantidad = int(cantidad)
            cursor.execute('insert into inventario (nombre_producto, precio, cantidad_disponible) values (%s,%s,%s)',(nombre,precio,cantidad))
            conexion.commit()
            QMessageBox.information( self, "Éxito", "Se agregó un nuevo producto")
        else:
            QMessageBox.warning( self, "Error", 'Datos Inválidos')


    @Slot()
    def click_buscar_modificar_inventario(self):
        nombreProducto = self.ui.lineEdit_buscar_modificar_inventario.text()
        encontrado = False
        cursor.execute("select *from inventario where nombre_producto = '{0}'".format(nombreProducto))
        inventario = cursor.fetchall()
        for producto in inventario:
            if producto[0] == nombreProducto:
                self.ui.tableWidget_inventario.clear()
                self.ui.tableWidget_inventario.setColumnCount(4)
                headers = ['Nombre del producto', 'Precio', 'Cantidad a pedir', 'Cantidad disponible']
                self.ui.tableWidget_inventario.setHorizontalHeaderLabels(headers)
                self.ui.tableWidget_inventario.setRowCount(1)
                nombre_producto_widget = QTableWidgetItem(str(producto[0]))
                precio_widget = QTableWidgetItem(str(producto[1]))
                cantidad_a_pedir_widget = QTableWidgetItem(str(producto[2]))
                cantidad_disponible_widget = QTableWidgetItem(str(producto[3]))
                self.ui.tableWidget_inventario.setItem(0,0,nombre_producto_widget)
                self.ui.tableWidget_inventario.setItem(0,1,precio_widget)
                self.ui.tableWidget_inventario.setItem(0,2,cantidad_a_pedir_widget)
                self.ui.tableWidget_inventario.setItem(0,3,cantidad_disponible_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'El producto no fue encontrado')  
        
    @Slot()
    def click_modificar_inventario(self):
        nombre = self.ui.lineEdit_agregar_modificar_inventario.text()
        precio = self.ui.lineEdit_precio_modificar_inventario.text()
        cantidad = self.ui.lineEdit_cantidad_modificar_inventario.text()
        nombreProducto = self.ui.lineEdit_buscar_modificar_inventario.text()
        cursor.execute("select *from inventario where nombre_producto = '{0}'".format(nombreProducto))
        inventario = cursor.fetchall()
        
        for producto in inventario:
            if producto[0] == nombreProducto:
                if int(cantidad.isnumeric()) == True and int(precio.isnumeric()) == True:
                    precio = int(precio)
                    cantidad = int(cantidad)
                    cursor.execute("update inventario set nombre_producto = '{0}' where nombre_producto = '{1}'".format(nombre, nombreProducto))
                    cursor.execute("update inventario set precio = '{0}' where nombre_producto = '{1}'".format(precio, nombreProducto))
                    cursor.execute("update inventario set cantidad_disponible = '{0}' where nombre_producto = '{1}'".format(cantidad, nombreProducto))
                    cursor.execute("update inventario set cantidad_a_pedir = 0 where nombre_producto = '{0}'".format(nombreProducto))
                    conexion.commit()
                    QMessageBox.information( self, "Éxito", "Se modificó el producto exitosamente")
                    encontrado = True
                    return
                else:
                    QMessageBox.warning( self, "Error", 'Datos Inválidos')    
        if not encontrado:
            QMessageBox.warning( self, "Error", 'El producto no fue encontrado')  
        


    
    @Slot()
    def click_ver_pedido(self):
        fechaPedido = self.ui.lineEdit_ver_pedidos.text()
        headers = ['Numero de pedido', 'Nombre del cliente', 'Teléfono del cliente', 'Fecha del pedido', 'Fecha de la entrega', 'Cantidad del pedido', 'Producto pedido']
        if fecha_valida(fechaPedido) == True:
            cursor.execute("select *from pedidos where fecha_entrega='{0}'".format(fechaPedido))
            pedidos = cursor.fetchall()
            if len(pedidos)>0:
                QMessageBox.information( self, "Éxito", "Se encontró la fecha")
            else:
                QMessageBox.warning( self, "Error", "Fecha no encontrada")
        else:
            cursor.execute('select *from pedidos')
            pedidos = cursor.fetchall()
            QMessageBox.information( self, "Búsqueda sin fecha", 'La fecha no fue introducida')  
        self.ui.tableWidget_pedidos.clear()
        self.ui.tableWidget_pedidos.setColumnCount(7)
        self.ui.tableWidget_pedidos.setRowCount(len(pedidos))
        row = 0
        self.ui.tableWidget_pedidos.setHorizontalHeaderLabels(headers)
        for pedido in pedidos:
            numero_pedido_widget = QTableWidgetItem(str(pedido[0]))
            nombre_cliente_widget = QTableWidgetItem(str(pedido[1]))
            telefono_cliente_widget = QTableWidgetItem(str(pedido[2]))
            fecha_pedido_widget = QTableWidgetItem(str(pedido[3]))
            fecha_entrega_widget = QTableWidgetItem(str(pedido[4]))
            cantidad_pedido_widget = QTableWidgetItem(str(pedido[5]))
            producto_pedido_widget = QTableWidgetItem(str(pedido[6]))
            self.ui.tableWidget_pedidos.setItem(row,0,numero_pedido_widget)
            self.ui.tableWidget_pedidos.setItem(row,1,nombre_cliente_widget)
            self.ui.tableWidget_pedidos.setItem(row,2,telefono_cliente_widget)
            self.ui.tableWidget_pedidos.setItem(row,3,fecha_pedido_widget)
            self.ui.tableWidget_pedidos.setItem(row,4,fecha_entrega_widget)
            self.ui.tableWidget_pedidos.setItem(row,5,cantidad_pedido_widget)
            self.ui.tableWidget_pedidos.setItem(row,6,producto_pedido_widget)
            row += 1
    
    @Slot()
    def click_buscar_pedido(self):
        numeroPedido = self.ui.lineEdit_buscar_pedidos.text()
        numeroPedido = int(numeroPedido)
        encontrado = False
        cursor.execute("select *from pedidos where numero_pedido = '{0}'".format(numeroPedido))
        pedidos = cursor.fetchall()
        for pedido in pedidos:
            if pedido[0] == numeroPedido:
                self.ui.tableWidget_pedidos.clear()
                self.ui.tableWidget_pedidos.setColumnCount(7)
                headers = ['Numero de pedido', 'Nombre del cliente', 'Teléfono del cliente', 'Fecha del pedido', 'Fecha de la entrega', 'Cantidad del pedido', 'Producto pedido']
                self.ui.tableWidget_pedidos.setHorizontalHeaderLabels(headers)
                self.ui.tableWidget_pedidos.setRowCount(1)
                numero_pedido_widget = QTableWidgetItem(str(pedido[0]))
                nombre_cliente_widget = QTableWidgetItem(str(pedido[1]))
                telefono_cliente_widget = QTableWidgetItem(str(pedido[2]))
                fecha_pedido_widget = QTableWidgetItem(str(pedido[3]))
                fecha_entrega_widget = QTableWidgetItem(str(pedido[4]))
                cantidad_pedido_widget = QTableWidgetItem(str(pedido[5]))
                producto_pedido_widget = QTableWidgetItem(str(pedido[6]))
                self.ui.tableWidget_pedidos.setItem(0,0,numero_pedido_widget)
                self.ui.tableWidget_pedidos.setItem(0,1,nombre_cliente_widget)
                self.ui.tableWidget_pedidos.setItem(0,2,telefono_cliente_widget)
                self.ui.tableWidget_pedidos.setItem(0,3,fecha_pedido_widget)
                self.ui.tableWidget_pedidos.setItem(0,4,fecha_entrega_widget)
                self.ui.tableWidget_pedidos.setItem(0,5,cantidad_pedido_widget)
                self.ui.tableWidget_pedidos.setItem(0,6,producto_pedido_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'El pedido no fue encontrado')     
    
    @Slot()
    def click_eliminar_pedido(self):
        numeroPedido = self.ui.lineEdit_buscar_pedidos.text()
        numeroPedido = int(numeroPedido)
        encontrado = False
        cursor.execute("select *from pedidos where numero_pedido = '{0}'".format(numeroPedido))
        pedidos = cursor.fetchall()
        for pedido in pedidos:
            if pedido[0] == numeroPedido:
                encontrado=True
                cursor.execute("delete from pedidos where numero_pedido = '{0}'".format(numeroPedido))
                conexion.commit()
                QMessageBox.information( self, "Éxito", "Pedido eliminado exitosamente")           
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'El pedido no fue encontrado')  

    @Slot()
    def click_agregar_pedido(self):
        nombre_cliente = self.ui.lineEdit_nombre_cliente_pedidos.text()
        telefono_cliente = self.ui.lineEdit_telefono_cliente_pedidos.text()
        fecha_pedido = self.ui.lineEdit_fecha_pedidos.text()
        fecha_entrega = self.ui.lineEdit_fecha_entrega_pedidos.text()
        cantidad = self.ui.lineEdit_cantidad_pedidos.text()
        nombre = self.ui.lineEdit_agregar_pedidos.text()
        
        cursor.execute("select nombre_producto, cantidad_disponible from inventario where nombre_producto='{0}'".format(nombre))
        
        validacion = cursor.fetchall()
        bandera = False
        for producto in validacion:
            if int(cantidad.isnumeric()) == True:
                if producto[0]==nombre and producto[1]>=int(cantidad):
                    bandera = True
        
        if int(cantidad.isnumeric()) == True and 10>=len(telefono_cliente)>=8 and fecha_valida(fecha_pedido) == True and fecha_valida(fecha_entrega) == True and bandera == True:
            cantidad = int(cantidad)
            cursor.execute('insert into pedidos (nombre_cliente, telefono_cliente, fecha_pedido, fecha_entrega, cantidad_pedido, producto_pedido) values (%s,%s,%s,%s,%s,%s)',(nombre_cliente, telefono_cliente, fecha_pedido, fecha_entrega, cantidad, nombre))
            cursor.execute("select cantidad_disponible, cantidad_a_pedir from inventario where nombre_producto='{0}'".format(nombre))
            cantidad_anterior = cursor.fetchall()
            cantidad_temporal = cantidad_anterior[0]
            cantidad_a_pedir = int(cantidad_temporal[1])+cantidad
            cantidad_nueva = int(cantidad_temporal[0])-cantidad
            cursor.execute("update inventario set cantidad_disponible='{0}' where nombre_producto='{1}'".format(cantidad_nueva, nombre))
            cursor.execute("update inventario set cantidad_a_pedir='{0}' where nombre_producto='{1}'".format(cantidad_a_pedir, nombre))
            conexion.commit()
            QMessageBox.information( self, "Éxito", "Se agregó un nuevo pedido")
        else:
            QMessageBox.warning( self, "Error", 'Datos Inválidos')
 
    @Slot()
    def click_buscar_modificar_pedido(self):
        numeroPedido = self.ui.lineEdit_buscar_modificar_pedidos.text()
        numeroPedido = int(numeroPedido)
        encontrado = False
        cursor.execute("select *from pedidos where numero_pedido = '{0}'".format(numeroPedido))
        pedidos = cursor.fetchall()
        for pedido in pedidos:
            if pedido[0] == numeroPedido:
                self.ui.tableWidget_pedidos.clear()
                self.ui.tableWidget_pedidos.setColumnCount(7)
                headers = ['Numero de pedido', 'Nombre del cliente', 'Teléfono del cliente', 'Fecha del pedido', 'Fecha de la entrega', 'Cantidad del pedido', 'Producto pedido']
                self.ui.tableWidget_pedidos.setHorizontalHeaderLabels(headers)
                self.ui.tableWidget_pedidos.setRowCount(1)
                numero_pedido_widget = QTableWidgetItem(str(pedido[0]))
                nombre_cliente_widget = QTableWidgetItem(str(pedido[1]))
                telefono_cliente_widget = QTableWidgetItem(str(pedido[2]))
                fecha_pedido_widget = QTableWidgetItem(str(pedido[3]))
                fecha_entrega_widget = QTableWidgetItem(str(pedido[4]))
                cantidad_pedido_widget = QTableWidgetItem(str(pedido[5]))
                producto_pedido_widget = QTableWidgetItem(str(pedido[6]))
                self.ui.tableWidget_pedidos.setItem(0,0,numero_pedido_widget)
                self.ui.tableWidget_pedidos.setItem(0,1,nombre_cliente_widget)
                self.ui.tableWidget_pedidos.setItem(0,2,telefono_cliente_widget)
                self.ui.tableWidget_pedidos.setItem(0,3,fecha_pedido_widget)
                self.ui.tableWidget_pedidos.setItem(0,4,fecha_entrega_widget)
                self.ui.tableWidget_pedidos.setItem(0,5,cantidad_pedido_widget)
                self.ui.tableWidget_pedidos.setItem(0,6,producto_pedido_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'El pedido no fue encontrado')                 
        
    @Slot()
    def click_modificar_pedido(self):
        numeroPedido = self.ui.lineEdit_buscar_modificar_pedidos.text()
        numeroPedido = int(numeroPedido)
        nombre_cliente = self.ui.lineEdit_nombre_cliente_modificar_pedidos.text()
        telefono_cliente = self.ui.lineEdit_telefono_cliente_modificar_pedidos.text()
        fecha_pedido = self.ui.lineEdit_fecha_modificar_pedidos.text()
        fecha_entrega = self.ui.lineEdit_fecha_entrega_modificar_pedidos.text()
        cantidad = self.ui.lineEdit_cantidad_modificar_pedidos.text()
        nombre = self.ui.lineEdit_agregar_modificar_pedidos.text()
        
        cursor.execute("select nombre_producto, cantidad_disponible from inventario where nombre_producto='{0}'".format(nombre))
        validacion = cursor.fetchall()
        cursor.execute("select cantidad_pedido from pedidos where numero_pedido='{0}'".format(numeroPedido))
        vendida = cursor.fetchall()
        cantidad_agregada = 0
        for v in vendida:
            cantidad_agregada = v[0]
        bandera = False
        for producto in validacion:
            if int(cantidad.isnumeric()) == True:
                if producto[0]==nombre and (producto[1]+cantidad_agregada)>=int(cantidad):
                    bandera = True
        
        if int(cantidad.isnumeric()) == True and 10>=len(telefono_cliente)>=8 and fecha_valida(fecha_pedido) == True and fecha_valida(fecha_entrega) == True and bandera == True:
            cursor.execute("select cantidad_pedido from pedidos where numero_pedido='{0}'".format(numeroPedido))
            modificable = cursor.fetchall()
            cantidadModificar = 0
            for m in modificable:
                cantidadModificar = m[0]
            cursor.execute("select cantidad_a_pedir, cantidad_disponible from inventario where nombre_producto='{0}'".format(nombre))
            cantidades = cursor.fetchall()
            for c in cantidades:
                cantidadPedir = c[0]
                cantidadDisponible = c[1]
            cantidadPedir -= cantidadModificar
            cantidadDisponible += cantidadModificar
            cursor.execute("update inventario set cantidad_a_pedir='{0}' where nombre_producto='{1}'".format(cantidadPedir, nombre))
            cursor.execute("update inventario set cantidad_disponible='{0}' where nombre_producto='{1}'".format(cantidadDisponible, nombre))
            conexion.commit()         
            cantidad = int(cantidad)
            cursor.execute("update pedidos set nombre_cliente='{0}' where numero_pedido='{1}'".format(nombre_cliente, numeroPedido))
            cursor.execute("update pedidos set telefono_cliente='{0}' where numero_pedido='{1}'".format(telefono_cliente, numeroPedido))            
            cursor.execute("update pedidos set fecha_pedido='{0}' where numero_pedido='{1}'".format(fecha_pedido, numeroPedido))            
            cursor.execute("update pedidos set fecha_entrega='{0}' where numero_pedido='{1}'".format(fecha_entrega, numeroPedido))            
            cursor.execute("update pedidos set cantidad_pedido='{0}' where numero_pedido='{1}'".format(cantidad, numeroPedido))            
            cursor.execute("update pedidos set producto_pedido='{0}' where numero_pedido='{1}'".format(nombre, numeroPedido))            
            cantidadPedir += cantidad
            cantidadDisponible -= cantidad
            cursor.execute("update inventario set cantidad_a_pedir='{0}' where nombre_producto='{1}'".format(cantidadPedir, nombre))
            cursor.execute("update inventario set cantidad_disponible='{0}' where nombre_producto='{1}'".format(cantidadDisponible, nombre))
            conexion.commit()               
            QMessageBox.information( self, "Éxito", "Se modificó un pedido")
        else:
            QMessageBox.warning( self, "Error", 'Datos Inválidos')

    
    
    @Slot()
    def click_ver_venta(self):
        fechaVenta = self.ui.lineEdit_ver_ventas.text()
        headers = ['Numero de venta', 'Cantidad vendida', 'Fecha de venta', 'Producto vendido']
        if fecha_valida(fechaVenta) == True:
            cursor.execute("select *from ventas where fecha_venta='{0}'".format(fechaVenta))
            ventas = cursor.fetchall()
            if len(ventas)>0:
                QMessageBox.information( self, "Éxito", "Se encontró la fecha")
            else:
                QMessageBox.warning( self, "Error", "Fecha no encontrada")
        else:
            cursor.execute('select *from ventas')
            ventas = cursor.fetchall()
            QMessageBox.information( self, "Búsqueda sin fecha", 'La fecha no fue introducida')  
        self.ui.tableWidget_ventas.clear()
        self.ui.tableWidget_ventas.setColumnCount(4)
        self.ui.tableWidget_ventas.setRowCount(len(ventas))
        row = 0
        self.ui.tableWidget_ventas.setHorizontalHeaderLabels(headers)
        for venta in ventas:
            numero_venta_widget = QTableWidgetItem(str(venta[0]))
            cantidad_venta_widget = QTableWidgetItem(str(venta[1]))
            fecha_venta_widget = QTableWidgetItem(str(venta[2]))
            nombre_producto_venta_widget = QTableWidgetItem(str(venta[3]))
            self.ui.tableWidget_ventas.setItem(row,0,numero_venta_widget)
            self.ui.tableWidget_ventas.setItem(row,1,cantidad_venta_widget)
            self.ui.tableWidget_ventas.setItem(row,2,fecha_venta_widget)
            self.ui.tableWidget_ventas.setItem(row,3,nombre_producto_venta_widget)
            row += 1
    
    @Slot()
    def click_buscar_venta(self):
        numeroVenta = self.ui.lineEdit_buscar_ventas.text()
        numeroVenta = int(numeroVenta)
        encontrado = False
        cursor.execute("select *from ventas where numero_venta = '{0}'".format(numeroVenta))
        ventas = cursor.fetchall()
        for venta in ventas:
            if venta[0] == numeroVenta:
                self.ui.tableWidget_ventas.clear()
                self.ui.tableWidget_ventas.setColumnCount(4)
                headers = ['Numero de venta', 'Cantidad vendida', 'Fecha de venta', 'Producto vendido']
                self.ui.tableWidget_ventas.setHorizontalHeaderLabels(headers)
                self.ui.tableWidget_ventas.setRowCount(1)
                numero_venta_widget = QTableWidgetItem(str(venta[0]))
                cantidad_venta_widget = QTableWidgetItem(str(venta[1]))
                fecha_venta_widget = QTableWidgetItem(str(venta[2]))
                nombre_producto_venta_widget = QTableWidgetItem(str(venta[3]))
                self.ui.tableWidget_ventas.setItem(0,0,numero_venta_widget)
                self.ui.tableWidget_ventas.setItem(0,1,cantidad_venta_widget)
                self.ui.tableWidget_ventas.setItem(0,2,fecha_venta_widget)
                self.ui.tableWidget_ventas.setItem(0,3,nombre_producto_venta_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'La venta no fue encontrada')     
    
    @Slot()
    def click_eliminar_venta(self):
        numeroVenta = self.ui.lineEdit_buscar_ventas.text()
        numeroVenta = int(numeroVenta)
        encontrado = False
        cursor.execute("select *from ventas where numero_venta = '{0}'".format(numeroVenta))
        ventas = cursor.fetchall()
        for venta in ventas:
            if venta[0] == numeroVenta:
                encontrado=True
                cursor.execute("delete from ventas where numero_venta = '{0}'".format(numeroVenta))
                conexion.commit()
                QMessageBox.information( self, "Éxito", "Venta eliminada exitosamente")           
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'La venta no fue encontrada') 
    
    @Slot()
    def click_agregar_venta(self):
        cantidad = self.ui.lineEdit_cantidad_ventas.text()
        fecha_venta = self.ui.lineEdit_fecha_ventas.text()
        nombre = self.ui.lineEdit_agregar_ventas.text()
        
        cursor.execute("select nombre_producto, cantidad_disponible from inventario where nombre_producto='{0}'".format(nombre))
        
        validacion = cursor.fetchall()
        bandera = False
        for producto in validacion:
            if int(cantidad.isnumeric()) == True:
                if producto[0]==nombre and producto[1]>=int(cantidad):
                    bandera = True
        
        if int(cantidad.isnumeric()) == True and fecha_valida(fecha_venta) == True and bandera == True:
            cantidad = int(cantidad)
            cursor.execute('insert into ventas (cantidad_vendida, fecha_venta, producto_venta) values (%s,%s,%s)',(cantidad, fecha_venta, nombre))
            cursor.execute("select cantidad_disponible, cantidad_a_pedir from inventario where nombre_producto='{0}'".format(nombre))
            cantidad_anterior = cursor.fetchall()
            cantidad_temporal = cantidad_anterior[0]
            cantidad_a_pedir = int(cantidad_temporal[1])+cantidad
            cantidad_nueva = int(cantidad_temporal[0])-cantidad
            cursor.execute("update inventario set cantidad_disponible='{0}' where nombre_producto='{1}'".format(cantidad_nueva, nombre))
            cursor.execute("update inventario set cantidad_a_pedir='{0}' where nombre_producto='{1}'".format(cantidad_a_pedir, nombre))
            conexion.commit()
            QMessageBox.information( self, "Éxito", "Se realizó una nueva venta")
        else:
            QMessageBox.warning( self, "Error", 'Datos Inválidos')
        
    @Slot()
    def click_ver_total_venta(self):
        fechaVenta = self.ui.lineEdit_ver_ventas.text()
        headers = ['Fecha de las ventas', 'Ganancias']
        if fecha_valida(fechaVenta) == True:
            ganancia = 0
            cursor.execute("select cantidad_vendida, producto_venta from ventas where fecha_venta='{0}'".format(fechaVenta))
            ventas = cursor.fetchall()
            for v in ventas:
                cursor.execute("select precio from inventario where nombre_producto='{0}'".format(v[1]))
                precio = cursor.fetchall()
                for p in precio:
                    precioInt = p[0]
                    precioInt = precioInt[1:]
                    ganancia += (int(v[0])*float(precioInt))
            cursor.execute("select cantidad_pedido, producto_pedido from pedidos where fecha_entrega='{0}'".format(fechaVenta))
            pedidos = cursor.fetchall()
            for p in pedidos:
                cursor.execute("select precio from inventario where nombre_producto='{0}'".format(p[1]))
                precio = cursor.fetchall()
                for pr in precio:
                    precioInt = pr[0]
                    precioInt = precioInt[1:]
                    ganancia += (int(p[0])*float(precioInt))             
            self.ui.tableWidget_ventas.clear()
            self.ui.tableWidget_ventas.setColumnCount(2)
            self.ui.tableWidget_ventas.setRowCount(1)
            self.ui.tableWidget_ventas.setHorizontalHeaderLabels(headers)
            fecha_ganancia_widget = QTableWidgetItem(str(fechaVenta))
            ganancia_widget = QTableWidgetItem('$'+str(ganancia))
            self.ui.tableWidget_ventas.setItem(0,0,fecha_ganancia_widget)
            self.ui.tableWidget_ventas.setItem(0,1,ganancia_widget)
        else:
            QMessageBox.warning( self, "Error", 'Fecha inválida')  
  
        
    @Slot()
    def click_buscar_modificar_venta(self):
        numeroVenta = self.ui.lineEdit_buscar_modificar_ventas.text()
        numeroVenta = int(numeroVenta)
        encontrado = False
        cursor.execute("select *from ventas where numero_venta = '{0}'".format(numeroVenta))
        ventas = cursor.fetchall()
        for venta in ventas:
            if venta[0] == numeroVenta:
                self.ui.tableWidget_ventas.clear()
                self.ui.tableWidget_ventas.setColumnCount(4)
                headers = ['Numero de venta', 'Cantidad vendida', 'Fecha de venta', 'Producto vendido']
                self.ui.tableWidget_ventas.setHorizontalHeaderLabels(headers)
                self.ui.tableWidget_ventas.setRowCount(1)
                numero_venta_widget = QTableWidgetItem(str(venta[0]))
                cantidad_venta_widget = QTableWidgetItem(str(venta[1]))
                fecha_venta_widget = QTableWidgetItem(str(venta[2]))
                nombre_producto_venta_widget = QTableWidgetItem(str(venta[3]))
                self.ui.tableWidget_ventas.setItem(0,0,numero_venta_widget)
                self.ui.tableWidget_ventas.setItem(0,1,cantidad_venta_widget)
                self.ui.tableWidget_ventas.setItem(0,2,fecha_venta_widget)
                self.ui.tableWidget_ventas.setItem(0,3,nombre_producto_venta_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning( self, "Error", 'La venta no fue encontrada')  
 
        
    @Slot()
    def click_modificar_venta(self):
        numeroVenta = self.ui.lineEdit_buscar_modificar_ventas.text()
        numeroVenta = int(numeroVenta)
        cantidad = self.ui.lineEdit_cantidad_modificar_ventas.text()
        fecha_venta = self.ui.lineEdit_fecha_modificar_ventas.text()
        nombre = self.ui.lineEdit_agregar_modificar_ventas.text()
        
        cursor.execute("select nombre_producto, cantidad_disponible from inventario where nombre_producto='{0}'".format(nombre))
        validacion = cursor.fetchall()
        cursor.execute("select cantidad_vendida from ventas where numero_venta='{0}'".format(numeroVenta))
        vendida = cursor.fetchall()
        cantidad_agregada = 0
        for v in vendida:
            cantidad_agregada = v[0]
        bandera = False
        for producto in validacion:
            if int(cantidad.isnumeric()) == True:
                if producto[0]==nombre and (producto[1]+cantidad_agregada)>=int(cantidad):
                    bandera = True
        
        if int(cantidad.isnumeric()) == True and fecha_valida(fecha_venta) == True and bandera == True:
            cursor.execute("select cantidad_vendida from ventas where numero_venta='{0}'".format(numeroVenta))
            modificable = cursor.fetchall()
            cantidadModificar = 0
            for m in modificable:
                cantidadModificar = m[0]
            cursor.execute("select cantidad_a_pedir, cantidad_disponible from inventario where nombre_producto='{0}'".format(nombre))
            cantidades = cursor.fetchall()
            for c in cantidades:
                cantidadPedir = c[0]
                cantidadDisponible = c[1]
            cantidadPedir -= cantidadModificar
            cantidadDisponible += cantidadModificar
            cursor.execute("update inventario set cantidad_a_pedir='{0}' where nombre_producto='{1}'".format(cantidadPedir, nombre))
            cursor.execute("update inventario set cantidad_disponible='{0}' where nombre_producto='{1}'".format(cantidadDisponible, nombre))
            conexion.commit()         
            cantidad = int(cantidad)
            cursor.execute("update ventas set cantidad_vendida='{0}' where numero_venta='{1}'".format(cantidad, numeroVenta))
            cursor.execute("update ventas set fecha_venta='{0}' where numero_venta='{1}'".format(fecha_venta, numeroVenta))
            cursor.execute("update ventas set producto_venta='{0}' where numero_venta='{1}'".format(nombre, numeroVenta))
            cantidadPedir += cantidad
            cantidadDisponible -= cantidad
            cursor.execute("update inventario set cantidad_a_pedir='{0}' where nombre_producto='{1}'".format(cantidadPedir, nombre))
            cursor.execute("update inventario set cantidad_disponible='{0}' where nombre_producto='{1}'".format(cantidadDisponible, nombre))
            conexion.commit()               
            QMessageBox.information( self, "Éxito", "Se modificó una venta")
        else:
            QMessageBox.warning( self, "Error", 'Datos Inválidos')
        
#cursor.close()
#conexion.close()
def fecha_valida(cadena):
    patron = '^(0\d|1[0-9]|2[0-9]|3[0-1])/(0\d|1[0-2])/20[0-9]{2}$'

    return bool(re.search(patron, cadena))
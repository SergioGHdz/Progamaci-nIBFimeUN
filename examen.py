import sys
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Pantalla1.ui", self)
        #Botones
        self.Boton1.clicked.connect(self.getChih)
        self.boton1up.clicked.connect(self.getup1)
        self.Boton2.clicked.connect(self.getCoah)
        self.boton2up.clicked.connect(self.getup2)
        self.Boton3.clicked.connect(self.getCol)
        self.boton3up.clicked.connect(self.getup3)
        self.Boton4.clicked.connect(self.getDur)
        self.boton4up.clicked.connect(self.getup4)
        self.Boton5.clicked.connect(self.getGto)
        self.boton5up.clicked.connect(self.getup5)
  
        
    def getChih(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="examen"
        )   
        mycursor = mydb.cursor()
        sql = "UPDATE Estado SET Numero_Estado  = '06' WHERE control = '1'"
        mydb.commit()
        mycursor.execute(sql)

        print("Buscando datos del estado del estado de Chihuahua.\n")
        sql2  = "SELECT \
          Datos_Estado.Estado AS ala, \
          Estado.Numero_Estado AS fav, \
          Datos_Estado.Confirmados AS conf, \
          Datos_Estado.Negativos AS neg, \
          Datos_Estado.Sospechosos AS sos, \
          Datos_Estado.Defunciones AS def, \
          Datos_Estado.Recuperados AS rec, \
          Datos_Estado.Activos AS act \
          FROM Datos_Estado\
          INNER JOIN Estado ON Datos_Estado.Num_Estado = Estado.Numero_Estado"
        mycursor.execute(sql2)
        
        myresult = mycursor.fetchall()

        for x in myresult:
            print('   Estado','   NumEst',' Conf', '  Neg','  Sosp',' Def',' Rec','  Act')
            print(x,"\n")

    def getup1(self):
        import commands
        result=commands.getoutput('/Users/Sergio3/Desktop/Python_Parcial Chih.py')

    
    def getCoah(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="examen"
        )   
        mycursor = mydb.cursor()
        sql = "UPDATE Estado SET Numero_Estado  = '07' WHERE control = '1'"
        mydb.commit()
        mycursor.execute(sql)

        print("Buscando datos del estado del estado de Coahuila.\n")
        sql2  = "SELECT \
          Datos_Estado2.Estado AS ala, \
          Estado.Numero_Estado AS fav, \
          Datos_Estado2.Confirmados AS conf, \
          Datos_Estado2.Negativos AS neg, \
          Datos_Estado2.Sospechosos AS sos, \
          Datos_Estado2.Defunciones AS def, \
          Datos_Estado2.Recuperados AS rec, \
          Datos_Estado2.Activos AS act \
          FROM Datos_Estado2\
          INNER JOIN Estado ON Datos_Estado2.Num_Estado = Estado.Numero_Estado"
        mycursor.execute(sql2)
        
        result = mycursor.fetchall()

        for x in result:
            print('   Estado','   NumEst',' Conf', '  Neg','  Sosp',' Def',' Rec','  Act')
            print(x,"\n")
            

    def getup2(self):
        
        result=commands.getoutput('/Users/Sergio3/Desktop/Python_Parcial Choah.py')


    def getCol(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="examen"
        )   
        mycursor = mydb.cursor()
        sql = "UPDATE Estado SET Numero_Estado  = '08' WHERE control = '1'"
        mydb.commit()
        mycursor.execute(sql)

        print("Buscando datos del estado del estado de Colima.\n")
        sql2  = "SELECT \
          Datos_Estado3.Estado AS ala, \
          Estado.Numero_Estado AS fav, \
          Datos_Estado3.Confirmados AS conf, \
          Datos_Estado3.Negativos AS neg, \
          Datos_Estado3.Sospechosos AS sos, \
          Datos_Estado3.Defunciones AS def, \
          Datos_Estado3.Recuperados AS rec, \
          Datos_Estado3.Activos AS act \
          FROM Datos_Estado3\
          INNER JOIN Estado ON Datos_Estado3.Num_Estado = Estado.Numero_Estado"
        mycursor.execute(sql2)
        
        result = mycursor.fetchall()

        for x in result:
            print('  Estado',' NumEst','Conf', '  Neg',' Sosp','Def',' Rec','  Act')
            print(x,"\n")

    def getup3(self):
        
        result=commands.getoutput('/Users/Sergio3/Desktop/Python_Parcial Col.py')

    def getDur(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="examen"
        )   
        mycursor = mydb.cursor()
        sql = "UPDATE Estado SET Numero_Estado  = '09' WHERE control = '1'"
        mydb.commit()
        mycursor.execute(sql)

        print("Buscando datos del estado de Durango.\n")
        sql2  = "SELECT \
          Datos_Estado4.Estado AS ala, \
          Estado.Numero_Estado AS fav, \
          Datos_Estado4.Confirmados AS conf, \
          Datos_Estado4.Negativos AS neg, \
          Datos_Estado4.Sospechosos AS sos, \
          Datos_Estado4.Defunciones AS def, \
          Datos_Estado4.Recuperados AS rec, \
          Datos_Estado4.Activos AS act \
          FROM Datos_Estado4\
          INNER JOIN Estado ON Datos_Estado4.Num_Estado = Estado.Numero_Estado"
        mycursor.execute(sql2)
        
        result = mycursor.fetchall()

        for x in result:
            print('  Estado',' NumEst',' Conf', '  Neg','  Sosp',' Def',' Rec','  Act')
            print(x,"\n")

    def getup4(self):
        
        result=commands.getoutput('/Users/Sergio3/Desktop/Python_Parcial Dur.py')


    def getGto(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="examen"
        )   
        mycursor = mydb.cursor()
        sql = "UPDATE Estado SET Numero_Estado  = '10' WHERE control = '1'"
        mydb.commit()
        mycursor.execute(sql)

        print("Buscando datos del estado de Guanajuato.\n")
        sql2  = "SELECT \
          Datos_Estado5.Estado AS ala, \
          Estado.Numero_Estado AS fav, \
          Datos_Estado5.Confirmados AS conf, \
          Datos_Estado5.Negativos AS neg, \
          Datos_Estado5.Sospechosos AS sos, \
          Datos_Estado5.Defunciones AS def, \
          Datos_Estado5.Recuperados AS rec, \
          Datos_Estado5.Activos AS act \
          FROM Datos_Estado5\
          INNER JOIN Estado ON Datos_Estado5.Num_Estado = Estado.Numero_Estado"
        mycursor.execute(sql2)
        
        result = mycursor.fetchall()

        for x in result:
            print('  Estado','      NumEst','Conf', '  Neg','  Sosp',' Def','   Rec','   Act')
            print(x,"\n")

    def getup5(self):
        
        result=commands.getoutput('/Users/Sergio3/Desktop/Python_Parcial Gto.py')

            
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


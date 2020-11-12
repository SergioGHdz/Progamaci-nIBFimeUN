import json
from tkinter import *
from tkinter.ttk import *


Chih={}
Chih['casos']=[]
Chih['casos'].append({
    'C.Confirmados':10988,
    'C.Negativos':10333,
    'C.Sospechosos':3634,
    'Defunciones':1377,
    'C.Recuperados':7324,
    'C.Activos':330
    })
Coah={}
Coah['casos']=[]
Coah['casos'].append({
    'C.Confirmados':26300,
    'C.Negativos':35405,
    'C.Sospechosos':3239,
    'Defunciones':1868,
    'C.Recuperados':21278,
    'C.Activos':1062
    })
Col={}
Col['casos']=[]
Col['casos'].append({
    'C.Confirmados':4831,
    'C.Negativos':3356,
    'C.Sospechosos':218,
    'Defunciones':526,
    'C.Recuperados':3207,
    'C.Activos':298
    })
Zac={}
Zac['casos']=[]
Zac['casos'].append({
    'C.Confirmados':7492,
    'C.Negativos':8624,
    'C.Sospechosos':192,
    'Defunciones':720,
    'C.Recuperados':5204,
    'C.Activos':545
    })
Dur={}
Dur['casos']=[]
Dur['casos'].append({
    'C.Confirmados':8854,
    'C.Negativos':15103,
    'C.Sospechosos':1472,
    'Defunciones':623,
    'C.Recuperados':6887,
    'C.Activos':581
    })
Gto={}
Gto['casos']=[]
Gto['casos'].append({
    'C.Confirmados':40655,
    'C.Negativos':55646,
    'C.Sospechosos':1970,
    'Defunciones':2894,
    'C.Recuperados':32543,
    'C.Activos':1323
    })
def estado():
    if (combo.get()) == 'Chihuahua':
        print("Estos son los casos en Chihuahua:")
        print(Chih['casos'])
        print(" ")
    elif (combo.get()) == 'Coahuila':
        print("Estos son los casos en Coahuila:")
        print(Coah['casos'])
        print(" ")
    elif (combo.get()) == 'Colima':
        print("Estos son los casos en Colima:")
        print(Col['casos'])
        print(" ")
    elif (combo.get()) == 'Durango':
        print("Estos son los casos en Durango:")
        print(Dur['casos'])
        print(" ")
    elif (combo.get()) == 'Guanajuato':
        print("Estos son los casos en Guanajuato:")
        print(Gto['casos'])
        print(" ")
def guardar():
    if combo.get()=='Chihuahua':
        with open('Chihcovid.json','w') as file:
            json.dump(Chih,file)
    elif combo.get()=='Coahuila':
        with open('Coahcovid.json','w') as file:
            json.dump(Coah,file)
    elif combo.get()=='Colima':
        with open('Colcovid.json','w') as file:
            json.dump(Col,file)
    elif combo.get()=='Durango':
        with open('Durcovid.json','w') as file:
            json.dump(Dur,file)
    else
        with open('Gtocovid.json','w') as file:
            json.dump(Gto,file)
    print("Los datos han sido guardados con exito")

windows = Tk()
windows.title('Covid Progra')
windows.geometry("300x300")

foto=PhotoImage(file='imagen1.png')
fondo=Label(windows,image=foto)
fondo.place(x=0,y=0)

texto=StringVar()
texto.set ('Estado: ')

combo = Combobox(windows)
combo.place(x=50,y=100)
combo['values'] = [
    'Chihuahua',
    'Coahuila',
    'Colima',
    'Durango',
    'Guanajuato'
    ]
combo.current()

boton=Button(windows,command=guardar,text='guardar datos')
btn=Button(windows,command=estado,text='entrar')
etiqueta=Label(windows,textvariable=texto)
etiqueta.place(x=40,y=200)

boton.place(x=175,y=150)
btn.place(x=75,y=150)


windows.mainloop()

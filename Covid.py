import json
from tkinter import *
from tkinter.ttk import *


Tam={}
Tam['casos']=[]
Tam['casos'].append({
    'C.Confirmados':29057,
    'C.Negativos':36222,
    'C.Sospechosos':2594,
    'Defunciones':2218,
    'C.Recuperados':23650,
    'C.Activos':616
    })
Ver={}
Ver['casos']=[]
Ver['casos'].append({
    'C.Confirmados':33480,
    'C.Negativos':18276,
    'C.Sospechosos':2597,
    'Defunciones':4369,
    'C.Recuperados':21036,
    'C.Activos':764
    })
Ytn={}
Ytn['casos']=[]
Ytn['casos'].append({
    'C.Confirmados':18451,
    'C.Negativos':17358,
    'C.Sospechosos':579,
    'Defunciones':1599,
    'C.Recuperados':13517,
    'C.Activos':927
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
Tlx={}
Tlx['casos']=[]
Tlx['casos'].append({
    'C.Confirmados':7539,
    'C.Negativos':13022,
    'C.Sospechosos':568,
    'Defunciones':1095,
    'C.Recuperados':5140,
    'C.Activos':78
    })
def estado():
    if (combo.get()) == 'Tamaulipas':
        print("Estos son los casos en Tamaulipas:")
        print(Tam['casos'])
        print(" ")
    elif (combo.get()) == 'Veracruz':
        print("Estos son los casos en Veracruz:")
        print(Ver['casos'])
        print(" ")
    elif (combo.get()) == 'Yucatan':
        print("Estos son los casos en Yucatan:")
        print(Ytn['casos'])
        print(" ")
    elif (combo.get()) == 'Zacatecas':
        print("Estos son los casos en Zacatecas:")
        print(Zac['casos'])
        print(" ")
    else:
         print("Estos son los casos en Tlaxcala:")
         print(Tlx['casos'])
         print(" ")
def guardar():
    if combo.get()=='Tamaulipas':
        with open('Tamcovid.json','w') as file:
            json.dump(Tam,file)
    elif combo.get()=='Veracruz':
        with open('Vercovid.json','w') as file:
            json.dump(Ver,file)
    elif combo.get()=='Yucatan':
        with open('Ytncovid.json','w') as file:
            json.dump(Ytn,file)
    elif combo.get()=='Zacatecas':
        with open('Zaccovid.json','w') as file:
            json.dump(Zac,file)
    else:
        with open('Tlxcovid.json','w') as file:
            json.dump(Tlx,file)
    print("Los datos han sido guardados con exito")

windows = Tk()
windows.title('Datos del COVID-19')
windows.geometry("300x300")

foto=PhotoImage(file='imagen1.png')
fondo=Label(windows,image=foto)
fondo.place(x=0,y=0)

texto=StringVar()
texto.set ('Estado: ')

combo = Combobox(windows)
combo.place(x=50,y=100)
combo['values'] = [
    'Tamaulipas',
    'Veracruz',
    'Yucatan',
    'Zacatecas',
    'Tlaxcala'
    ]
combo.current()

boton=Button(windows,command=guardar,text='guardar datos')
btn=Button(windows,command=estado,text='entrar')
etiqueta=Label(windows,textvariable=texto)
etiqueta.place(x=40,y=200)

boton.place(x=175,y=150)
btn.place(x=75,y=150)


windows.mainloop()

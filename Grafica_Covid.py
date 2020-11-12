import matplotlib.pyplot as plt


Est = ['Chihuahua', 'Coahuila', 'Colima', 'Durango', ' Guanajuato','Sumatoria']
Defunciones = (1377, 1868, 526, 623,2894, 7288)
colores = ('purple', 'red', 'green', 'yellow', 'cyan', 'gray')

plt.barh(range(6),Defunciones,color=colores)
plt.yticks(range(6), Est, rotation = 60)
plt.title ("Comparacion de defunciones por Covid-19")
plt.xlim(min(Defunciones)-20,max(Defunciones)+100)
plt.show()
